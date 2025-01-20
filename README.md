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

## How It Works

1. The script generates all possible domain names with lengths ranging from a minimum to a maximum value using `itertools.product`.
2. For each domain, it runs the `whois` command to check its availability.
3. If the `whois` output contains "No match for domain", the domain is deemed available and written to the output file.
4. A progress bar updates in real-time, showing the progress of checks and statistics.

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
   git clone https://github.com/diGiCTF/domain-availability-checker.git
   cd domain-availability-checker
