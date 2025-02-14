import itertools
import subprocess
import random
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# List of alternative WHOIS servers
WHOIS_SERVERS = [
    "whois.verisign-grs.com",  # Good for .com, .net
    "whois.nic.ai",            # .ai domains
    "whois.iana.org",          # General WHOIS fallback
    "whois.pir.org",           # .org domains
    "whois.nic.io",            # .io domains
    "whois.nic.co",            # .co domains
]

# List of alternative DNS resolvers
DNS_RESOLVERS = [
    "1.1.1.1",  # Cloudflare
    "8.8.8.8",  # Google
    "9.9.9.9",  # Quad9
    "208.67.222.222",  # OpenDNS
]

def resolve_domain(domain):
    """Attempts to resolve a domain using a random DNS resolver before WHOIS lookup."""
    dns_resolver = random.choice(DNS_RESOLVERS)
    try:
        subprocess.run(["nslookup", domain, dns_resolver], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except Exception as e:
        print(f"DNS resolution failed for {domain} using {dns_resolver}: {e}")

def check_domain(domain):
    """Runs WHOIS on a domain using a random WHOIS server and returns its availability."""
    whois_server = random.choice(WHOIS_SERVERS)
    
    try:
        process = subprocess.Popen(
            ["whois", "-h", whois_server, domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, _ = process.communicate()

        if "No match for domain" in stdout or "NOT FOUND" in stdout or "Domain not found" in stdout:
            return domain  # Domain is available
    except Exception as e:
        print(f"Error checking {domain} with {whois_server}: {e}")
    
    return None  # Domain is not available

def check_domain_availability(output_file="domaincheck.txt", max_workers=10):
    """Main function to check domain availability efficiently using multiple WHOIS servers."""

    # User input for domain extension
    domain_ext_input = input("What domain extension would you like to check (com, ai)? ").strip()
    domain_extension = "." + domain_ext_input.lstrip(".")

    # User input for length range
    min_length = int(input("Enter minimum length to check for (default 1): ").strip() or 1)
    max_length = int(input("Enter maximum length to check for (default 3): ").strip() or 3)

    # User input for character set
    characters = input("Enter characters to use for generating domain names (default: abcdefghijklmnopqrstuvwxyz0123456789): ").strip()
    if not characters:
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"

    # Generate all possible domain names
    domains = [
        "".join(comb) + domain_extension
        for length in range(min_length, max_length + 1)
        for comb in itertools.product(characters, repeat=length)
    ]

    total_checked = 0
    available_domains = []

    with open(output_file, "w") as file, ThreadPoolExecutor(max_workers=max_workers) as executor:
        with tqdm(total=len(domains), desc="Checking domains", smoothing=0.1) as pbar:
            futures = {executor.submit(check_domain, domain): domain for domain in domains}

            for future in as_completed(futures):
                total_checked += 1
                domain_result = future.result()
                
                if domain_result:
                    available_domains.append(domain_result)
                    file.write(domain_result + "\n")
                    file.flush()

                # Update progress bar smoothly
                pbar.set_postfix(checked=total_checked, available=len(available_domains))
                pbar.update(1)

                # Small sleep to avoid WHOIS rate limiting (adjust if necessary)
                time.sleep(0.05)

    print(f"Domain check completed. Total checked: {total_checked}, Available found: {len(available_domains)}.")
    print(f"Available domains saved to {output_file}.")

if __name__ == "__main__":
    check_domain_availability()
