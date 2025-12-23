#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from colorama import Fore, Style
import requests
from bs4 import BeautifulSoup

# -------------------------
# Logging Setup
# -------------------------
logging.basicConfig(
    filename="reconkit.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# -------------------------
# ASCII Banner
# -------------------------
def print_banner():
    banner = r"""
 
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗██╗████████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██║ ██╔╝██║╚══██╔══╝
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║   
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║  
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║  ██╗██║   ██║ 
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝   ╚═╝ 
"""
    print(Fore.CYAN + banner + Style.RESET_ALL)
    print(Fore.GREEN + "Reconnaissance Framework for Bug Bounty" + Style.RESET_ALL)
    print(Fore.YELLOW + "Built by Purushotham R\n" + Style.RESET_ALL)

# -------------------------
# Man Page
# -------------------------
def show_man():
    man_text = """
RECONKIT(1) ReconKit Manual

NAME
    reconkit - Personal Reconnaissance Framework for Bug Bounty

SYNOPSIS
    reconkit -d <domain> [OPTIONS]

DESCRIPTION
    ReconKit automates subdomain enumeration, live host detection,
    JS endpoint extraction, Nuclei scanning, reflected parameter detection,
    and supports Slack/Discord notifications.

OPTIONS
    -d, --domain <domain>       Target domain (required)
    --subs                       Run subdomain enumeration only
    --live                       Detect live hosts
    --js                         Extract JavaScript endpoints
    --nuclei                     Run Nuclei smart templates
    --reflected                  Detect reflected parameters
    --scope <file>               Provide a scope file
    --update                     Update ReconKit to latest version
    -o, --output <dir>           Output directory
    -h, --help                   Show help
    --man                        Show this man page

AUTHOR
    Purushotham R — Security Researcher | Bug Bounty Hunter
"""
    print(man_text)
    sys.exit(0)

# -------------------------
# JS Endpoint Extraction
# -------------------------
async def extract_js_endpoints(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        scripts = [s.get("src") for s in soup.find_all("script") if s.get("src")]
        return scripts
    except Exception as e:
        logging.error(f"JS extraction failed for {url}: {e}")
        return []

# -------------------------
# Parallel execution
# -------------------------
async def run_parallel(tasks):
    results = await asyncio.gather(*tasks)
    return results

# -------------------------
# Main CLI
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="ReconKit: Bug Bounty Recon Framework")
    parser.add_argument("-d", "--domain", help="Target domain")
    parser.add_argument("--subs", action="store_true", help="Run subdomain enumeration")
    parser.add_argument("--live", action="store_true", help="Detect live hosts")
    parser.add_argument("--js", action="store_true", help="Extract JS endpoints")
    parser.add_argument("--nuclei", action="store_true", help="Run Nuclei smart templates")
    parser.add_argument("--reflected", action="store_true", help="Detect reflected parameters")
    parser.add_argument("--scope", help="Provide scope file")
    parser.add_argument("--update", action="store_true", help="Update ReconKit")
    parser.add_argument("-o", "--output", help="Output directory", default="output")
    parser.add_argument("--man", action="store_true", help="Show man page")
    args = parser.parse_args()

    if args.man:
        show_man()

    if not args.domain and not args.update:
        parser.print_help()
        sys.exit(1)

    print_banner()

    if args.update:
        print(Fore.CYAN + "[*] Updating ReconKit..." + Style.RESET_ALL)
        # Placeholder for update logic
        sys.exit(0)

    # Ensure output directory exists
    domain_dir = os.path.join(args.output, args.domain)
    os.makedirs(domain_dir, exist_ok=True)

    # JS extraction example
    if args.js:
        print(Fore.GREEN + f"[*] Extracting JS endpoints from {args.domain}..." + Style.RESET_ALL)
        urls = [f"https://{args.domain}"]
        loop = asyncio.get_event_loop()
        tasks = [extract_js_endpoints(u) for u in urls]
        results = loop.run_until_complete(run_parallel(tasks))
        for js_list in results:
            for js in js_list:
                print(Fore.YELLOW + f"JS: {js}" + Style.RESET_ALL)
                with open(os.path.join(domain_dir, "js_endpoints.txt"), "a") as f:
                    f.write(js + "\n")

    # Placeholder for other modules (subs, live, nuclei, reflected)
    if args.subs:
        print(Fore.CYAN + "[*] Running subdomain enumeration..." + Style.RESET_ALL)

    if args.live:
        print(Fore.CYAN + "[*] Detecting live hosts..." + Style.RESET_ALL)

    if args.nuclei:
        print(Fore.CYAN + "[*] Running Nuclei scans..." + Style.RESET_ALL)

    if args.reflected:
        print(Fore.CYAN + "[*] Detecting reflected parameters..." + Style.RESET_ALL)

    print(Fore.GREEN + "[+] ReconKit completed!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
