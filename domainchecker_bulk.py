import subprocess
from tqdm import tqdm

# Made by https://github.com/diGiCTF
# Version 3

def check_domain_availability(input_file="domainchecker_import.txt", output_file="domaincheck_results.txt"):
    print(f"Please list all the domains you want to check in {input_file}.")
    
    try:
        with open(input_file, "r") as file:
            domains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please create the file and add domains to check.")
        return
    
    if not domains:
        print("No domains found in the input file. Please add domains and try again.")
        return
    
    total_checked = 0
    available_domains = []
    
    with tqdm(total=len(domains), desc="Checking domains") as pbar, open(output_file, "w") as output:
        for domain in domains:
            try:
                result = subprocess.run(
                    ["whois", domain],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
                total_checked += 1
                
                if "No match for domain" in result.stdout:
                    available_domains.append(domain)
                    output.write(domain + "\n")
                    output.flush()
            except Exception as e:
                print(f"Error checking domain {domain}: {e}")
            
            pbar.set_postfix(checked=total_checked, available=len(available_domains))
            pbar.update(1)
    
    print(f"Domain check completed. Total checked: {total_checked}, Available: {len(available_domains)}.")
    if available_domains:
        print("Available domains:")
        for domain in available_domains:
            print(domain)
    else:
        print("No available domains found.")
    
    print(f"Results saved to {output_file}.")

if __name__ == "__main__":
    check_domain_availability()
