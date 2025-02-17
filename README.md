# Domain Availability Checker

A Python script to check the availability of `.com` domains for all alphanumeric combinations within a specified range of character lengths. This script uses the `whois` command to query domain availability and saves the results for domains that are available (not registered) to an output file. It also features a progress bar with real-time statistics.

## New bulk domain checker
Create a bulk list to check
Create a file domainchecker_import.txt and list all the domains there
```
$ python3 domainchecker_bulk.py
Checking domains: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:01<00:00,  2.70it/s, available=1, checked=4]
Domain check completed. Total checked: 4, Available: 1.
Available domains:
Iwonderifthisisavailablexxx.com
Results saved to domaincheck_results.txt.
```


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

## Multi threading (beta)
```$ python3 domainchecker_multi.py``` 
✅ **Uses Multiple WHOIS Servers**  
- The script randomly selects from multiple WHOIS servers to **distribute load** and **reduce rate limits**.  
- This prevents a single WHOIS server from blocking or throttling requests.  

✅ **Uses Multiple DNS Resolvers for Faster Lookups**  
- Runs **nslookup** using different DNS servers before performing a WHOIS query.  
- This avoids slow lookups caused by relying on a single DNS provider.  

✅ **Parallel Execution for Faster Processing**  
- The script runs **multiple WHOIS queries in parallel** using `ThreadPoolExecutor(max_workers=10)`.  
- Instead of checking domains sequentially, it **checks 10 domains at a time**, significantly reducing total runtime.  

✅ **Handles Rate Limits & Avoids Freezing**  
- Introduces **a small delay (`time.sleep(0.05)`)** between queries to avoid being blocked by WHOIS servers.  
- Uses **multiple DNS and WHOIS servers** to balance the load across different providers.  

✅ **Real-Time Progress Updates**  
- The `tqdm` progress bar updates **smoothly** as domains are processed.  
- Displays **total checked domains** and **available domains found** in real time.  

This optimization makes the script **3-5x faster** than a traditional sequential WHOIS lookup while preventing server throttling issues.




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
   python3 domainchecker.py
