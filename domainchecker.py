import itertools
import subprocess
from tqdm import tqdm
#Made by https://github.com/diGiCTF
#Version 2

def check_domain_availability(output_file="domaincheck.txt"):
    # Ask user for domain extension and normalize it to start with a dot.
    domain_ext_input = input("What domain extension would you like to check (com, ai)? ").strip()
    if not domain_ext_input.startswith("."):
        domain_extension = "." + domain_ext_input
    else:
        domain_extension = domain_ext_input

    # Ask user for the minimum length to check for (default is 1)
    min_length_input = input("Enter minimum length to check for (default 1): ").strip()
    min_length = int(min_length_input) if min_length_input else 1

    # Ask user for the maximum length to check for (default is 3)
    max_length_input = input("Enter maximum length to check for (default 3): ").strip()
    max_length = int(max_length_input) if max_length_input else 3

    # Ask user for characters to use; if no input, default to "abcdefghijklmnopqrstuvwxyz0123456789"
    characters_input = input("Enter characters to use for generating domain names (default: abcdefghijklmnopqrstuvwxyz0123456789): ").strip()
    characters = characters_input if characters_input else "abcdefghijklmnopqrstuvwxyz0123456789"

    total_checked = 0  # Tracks total domains checked
    available_count = 0  # Tracks total available domains found

    with open(output_file, "w") as file:
        for length in range(min_length, max_length + 1):
            combinations = itertools.product(characters, repeat=length)
            combinations_count = len(characters) ** length

            # Progress bar for current length combinations
            with tqdm(total=combinations_count, desc=f"Checking {length}-char domains") as pbar:
                for combination in combinations:
                    domain = "".join(combination) + domain_extension
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
                    pbar.set_postfix(total_checked=total_checked, available_found=available_count)
                    pbar.update(1)

    print(f"Domain check completed. Total checked: {total_checked}, Available found: {available_count}.")
    print(f"Available domains saved to {output_file}.")

if __name__ == "__main__":
    check_domain_availability()
