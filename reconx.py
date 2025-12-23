#!/usr/bin/env python3
"""
ReconX v1.0 - Bug Bounty Focused Recon CLI
Developed by Purushotham R
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import time

# --------------- CONFIG ----------------
CONFIG_FILE = "reconx_config.cfg"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ---------------- ANIMATION ----------------
def animate_text(text, delay=0.05):
    for c in text:
        print(f"{CYAN}{c}{RESET}", end="", flush=True)
        time.sleep(delay)
    print("\n")

def banner():
animate_text(
        "\n"
        "██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗\n"
        "██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝\n"
        "██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ \n"
        "██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ \n"
        "██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗\n"
        "╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝\n"
    )

    animate_text("Reconnaissance Framework for Bug Bounty\n")
    animate_text("Developed by Purushotham R\n", delay=0.08)

# ---------------- LOGGING ----------------
def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color = GREEN if level=="INFO" else RED
    print(f"{color}[{timestamp}] {message}{RESET}")

# ---------------- UTILS ----------------
def run(cmd):
    log(f"Running: {cmd}", "INFO")
    return subprocess.run(cmd, shell=True)

# Dependency check
def check_dependencies(tools):
    for tool in tools:
        if not shutil.which(tool):
            log(f"{tool} not found! Install it first.", "ERROR")
            sys.exit(1)

# ---------------- MODULES ----------------
def subdomain_enum(domain, out_dir):
    log("Starting Subdomain Enumeration")
    all_subs = f"{out_dir}/subdomains_all.txt"
    final_subs = f"{out_dir}/subdomains.txt"

    cmds = [
        f"subfinder -d {domain} -silent >> {all_subs}",
        f"amass enum -passive -d {domain} >> {all_subs}",
        f"sublist3r -d {domain} -o /tmp/reconx_subs.txt",
        f"cat /tmp/reconx_subs.txt >> {all_subs}",
        f"dnsrecon -d {domain} -t brt >> {all_subs}",
        f"sort -u {all_subs} > {final_subs}"
    ]
    for cmd in cmds:
        run(cmd)
    log(f"Subdomains saved to {final_subs}")

def live_hosts(out_dir):
    log("Checking Live Hosts")
    subs = f"{out_dir}/subdomains.txt"
    live = f"{out_dir}/live_hosts.txt"
    if not os.path.exists(subs):
        log("Subdomains not found. Run --subs first.", "ERROR")
        return
    run(f"httpx -l {subs} -silent -o {live}")
    log(f"Live hosts saved to {live}")

def js_recon(out_dir):
    log("Starting JavaScript Recon")
    # placeholder for JS analysis
    # extract JS files + endpoints
    log("JS analysis completed (placeholder)")

def nuclei_scan(out_dir):
    log("Starting Nuclei Scan")
    # placeholder for smart templates
    log("Nuclei scan completed (placeholder)")

def reflected_param_check(out_dir):
    log("Checking Reflected Params")
    # placeholder
    log("Reflected param detection completed (placeholder)")

def slack_notify(message):
    # placeholder for Slack/Discord webhook
    log(f"Notification sent: {message}")

# ---------------- PARALLEL EXECUTION ----------------
def run_parallel(functions):
    with ThreadPoolExecutor(max_workers=len(functions)) as executor:
        futures = [executor.submit(func) for func in functions]
        for f in futures:
            f.result()

# ---------------- MAIN ----------------
def main():
    banner()

    parser = argparse.ArgumentParser(
        description="ReconX v1.0 - Bug bounty recon CLI"
    )
    parser.add_argument("-d","--domain",help="Target domain")
    parser.add_argument("--subs",action="store_true",help="Run subdomain enumeration")
    parser.add_argument("--live",action="store_true",help="Check live hosts")
    parser.add_argument("--js",action="store_true",help="JS recon")
    parser.add_argument("--nuclei",action="store_true",help="Nuclei scan")
    parser.add_argument("--reflected",action="store_true",help="Reflected param detection")
    parser.add_argument("--all",action="store_true",help="Run full recon")
    parser.add_argument("-o","--output",help="Output directory")
    parser.add_argument("--scope",help="Scope file")
    args = parser.parse_args()

    if not args.domain:
        parser.print_help()
        sys.exit(1)

    out_dir = args.output if args.output else f"output/{args.domain}"
    os.makedirs(out_dir, exist_ok=True)

    tasks = []
    if args.all or args.subs:
        tasks.append(lambda: subdomain_enum(args.domain, out_dir))
    if args.all or args.live:
        tasks.append(lambda: live_hosts(out_dir))
    if args.all or args.js:
        tasks.append(lambda: js_recon(out_dir))
    if args.all or args.nuclei:
        tasks.append(lambda: nuclei_scan(out_dir))
    if args.all or args.reflected:
        tasks.append(lambda: reflected_param_check(out_dir))

    # Run selected modules in parallel
    run_parallel(tasks)

    slack_notify(f"ReconX completed for {args.domain}")

    log("ReconX finished!", "INFO")
    log(f"Results in {out_dir}")

if __name__=="__main__":
    import shutil
    main()
