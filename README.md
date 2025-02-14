# Domain Availability Checker

A Python script to check the availability of `.com` domains for all alphanumeric combinations within a specified range of character lengths. This script uses the `whois` command to query domain availability and saves the results for domains that are available (not registered) to an output file. It also features a progress bar with real-time statistics.

## Features

- **Customizable Character Range**: Check domain names from a minimum to a maximum character length (default: 9–12 characters).
- **Alphanumeric Combinations**: Generates combinations of `a-z` and `0-9` to construct domain names.
- **WHOIS Integration**: Uses the `whois` command to check if a domain is registered.
- **Progress Bar**: Displays progress for each character length, including:
  - Total domains checked
  - Number of available domains found
- **Output File**: Saves available domains to `domaincheck.txt`.
- You can change the .com extension to other extensions i.e. .co, .net, .org etc

## How It Works (Version 2 - released 2/14/2025) 

1. The script prompts the user for the domain extension to check (e.g., `.com`, `.ai`). If the user enters `ai` or `.ai`, it ensures the extension starts with a dot.
2. The script asks for the minimum and maximum length of domain names to generate. If left blank, defaults are used (`1` for minimum and `3` for maximum).
3. The script prompts the user for a custom character set to generate domain names. If no input is provided, it defaults to `"abcdefghijklmnopqrstuvwxyz0123456789"`.
4. Using `itertools.product`, the script generates all possible domain names within the specified length range using the chosen character set.
5. Each generated domain is checked for availability using the `whois` command.
6. If the `whois` output contains "No match for domain", the domain is deemed available and written to the output file.
7. A progress bar updates in real-time, displaying the number of domains checked and the number of available domains found.


## Note
Before purchasing a short domain, research its history. Some may have high spam ratings, making them better to avoid.

## Prerequisites

- Python 3.x
- `whois` command-line tool installed on your system
- `tqdm` Python library (for progress bars)
  - Install with: `pip install tqdm`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/diGiCTF/domainchecker.git
   cd domainchecker
   python3 domainchecker.py```
