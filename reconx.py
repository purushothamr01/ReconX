#!/usr/bin/env python3
"""
ReconX v1.0
Reconnaissance Framework for Bug Bounty
Developed by Purushotham R
"""

import argparse
import os
import subprocess
import sys
import time
import shutil
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ---------------- COLORS ----------------
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ---------------- ANIMATION ----------------
def animate_text(text, delay=0.03):
    for c in text:
        print(f"{CYAN}{c}{RESET}", end="", flush=True)
        time.sleep(delay)
    print()

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
def log(msg, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color = GREEN if level == "INFO" else RED
    print(f"{color}[{ts}] {msg}{RESET}")

# ---------------- UTILS ----------------
def run(cmd, silent=False):
    log(cmd)
    return subprocess.run(cmd, shell=True,
        stdout=subprocess.DEVNULL if silent else None,
        stderr=subprocess.DEVNULL if silent else None
    )

def check_dep(tool):
    if not shutil.which(tool):
        log(f"Missing dependency: {tool}", "ERROR")
        sys.exit(1)

# ---------------- MODULES ----------------
def subdomains(domain, out):
    allf = f"{out}/subdomains_all.txt"
    finalf = f"{out}/subdomains.txt"

    cmds = [
        f"subfinder -d {domain} -silent >> {allf}",
        f"amass enum -passive -d {domain} >> {allf}",
        f"sublist3r -d {domain} -o /tmp/reconx_subs.txt",
        f"cat /tmp/reconx_subs.txt >> {allf}",
        f"dnsrecon -d {domain} -t brt >> {allf}",
        f"sort -u {allf} > {finalf}"
    ]
    for c in cmds:
        run(c, silent=True)

def live_hosts(out):
    run(f"httpx -l {out}/subdomains.txt -silent -o {out}/live.txt")

def url_collection(domain, out):
    run(f"gau {domain} > {out}/urls.txt", silent=True)
    run(f"waybackurls {domain} >> {out}/urls.txt", silent=True)
    run(f"sort -u {out}/urls.txt -o {out}/urls.txt")

def js_endpoints(out):
    js_file = f"{out}/js_files.txt"
    endpoints = f"{out}/js_endpoints.txt"

    run(f"grep -i '\\.js' {out}/urls.txt | sort -u > {js_file}")
    run(f"linkfinder -i {js_file} -o cli > {endpoints}")

def nuclei_smart(out):
    run(
        f"nuclei -l {out}/live.txt "
        f"-severity high,critical "
        f"-o {out}/nuclei.txt"
    )

# ---------------- UPDATE ----------------
def self_update():
    log("Updating ReconX...")
    run("git pull")
    log("ReconX updated successfully")

# ---------------- MAIN ----------------
def main():
    banner()

    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--domain")
    parser.add_argument("--subs", action="store_true")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--urls", action="store_true")
    parser.add_argument("--js", action="store_true")
    parser.add_argument("--nuclei", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--update", action="store_true")
    args = parser.parse_args()

    if args.update:
        self_update()
        return

    if not args.domain:
        parser.print_help()
        sys.exit(1)

    out = f"output/{args.domain}"
    os.makedirs(out, exist_ok=True)

    check_dep("subfinder")
    check_dep("httpx")

    tasks = []

    if args.all or args.subs:
        tasks.append(lambda: subdomains(args.domain, out))
    if args.all or args.live:
        tasks.append(lambda: live_hosts(out))
    if args.all or args.urls:
        tasks.append(lambda: url_collection(args.domain, out))
    if args.all or args.js:
        tasks.append(lambda: js_endpoints(out))
    if args.all or args.nuclei:
        tasks.append(lambda: nuclei_smart(out))

    with ThreadPoolExecutor(max_workers=5) as ex:
        ex.map(lambda f: f(), tasks)

    log("ReconX finished successfully")

if __name__ == "__main__":
    main()
