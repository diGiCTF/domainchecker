# Domain Availability Checker Scripts

This repository contains a collection of Python scripts designed to check the availability of domain names efficiently. Each script serves a slightly different purpose and provides unique features for domain availability checking.

## Scripts Overview

### 1. `domainchecker_bulk.py`
- **Purpose**: Checks the availability of a list of domains from a file.
- **How It Works**:
  - Reads domain names from `domainchecker_import.txt`.
  - Uses the `whois` command to check each domain.
  - Displays a progress bar with statistics on checked and available domains.
  - Saves available domains to `domaincheck_results.txt`.
- **Best For**: Bulk checking pre-defined domain lists.

### 2. `domainchecker.py`
- **Purpose**: Generates and checks domain name availability based on user-defined criteria.
- **How It Works**:
  - Asks for a domain extension (e.g., `.com`, `.ai`).
  - Allows users to specify the minimum and maximum domain length.
  - Users can define a custom character set for domain generation.
  - Iterates through all possible combinations and checks availability using `whois`.
  - Saves available domains to `domaincheck.txt`.
- **Best For**: Checking all possible domain combinations within a given length range.

### 3. `domainchecker_multi.py`
- **Purpose**: Optimized, multi-threaded domain checker using multiple WHOIS servers and DNS resolvers.
- **How It Works**:
  - Asks for a domain extension, length range, and character set.
  - Uses `ThreadPoolExecutor` to check multiple domains in parallel.
  - Randomly selects WHOIS servers to avoid rate-limiting issues.
  - Implements DNS resolution before WHOIS lookup for improved efficiency.
  - Saves available domains to `domaincheck.txt`.
- **Best For**: Fast and distributed domain availability checking across different WHOIS servers.

## Requirements
Ensure you have the following installed before running any of the scripts:
- Python 3
- `whois` command-line tool
- `tqdm` for progress bars (`pip install tqdm`)

## Usage
Run any script with:
```bash
python script_name.py
