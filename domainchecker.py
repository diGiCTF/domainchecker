import itertools
import subprocess
from tqdm import tqdm

def check_domain_availability(output_file="domaincheck.txt"):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    min_length = 1  # Start checking from 9 characters
    max_length = 5  # Check up to 12 characters
    total_checked = 0  # Tracks total domains checked
    available_count = 0  # Tracks total available domains found

    with open(output_file, "w") as file:
        for length in range(min_length, max_length + 1):  # Adjusted range
            combinations = itertools.product(characters, repeat=length)
            combinations_count = len(characters) ** length

            # Progress bar for current length combinations
            with tqdm(total=combinations_count, desc=f"Checking {length}-char domains") as pbar:
                for combination in combinations:
                    domain = "".join(combination) + ".com"
                    try:
                        # Execute whois command
                        result = subprocess.run(
                            ["whois", domain],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                        )
                        total_checked += 1  # Increment total domains checked
                        
                        if "No match for domain" in result.stdout:
                            # Save available domain
                            available_count += 1
                            file.write(domain + "\n")
                            file.flush()
                    except Exception as e:
                        print(f"Error checking domain {domain}: {e}")
                    
                    # Update the progress bar description with real-time stats
                    pbar.set_postfix(
                        total_checked=total_checked, available_found=available_count
                    )
                    pbar.update(1)

    print(f"Domain check completed. Total checked: {total_checked}, Available found: {available_count}.")
    print(f"Available domains saved to {output_file}.")

if __name__ == "__main__":
    check_domain_availability()
