# ReconX 🔎
### A Personal Reconnaissance Framework for Bug Bounty

    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗
    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝
    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ 
    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ 
    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗
    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝

    

A personal recon framework I built while hunting bugs, breaking apps, and actually reading JavaScript.
Not a wrapper. Not a copy.
Just the workflow that worked for me — automated, refined, and battle‑tested.

Crafted in terminals, tested on real targets.
Built by Purushotham R

## 🧠 Why ReconX?

Most recon tools run everything and drown you in noise.
ReconX focuses on signal over volume.

Read JavaScript, don’t ignore it

Scan what matters, not everything

Keep recon fast, clean, and repeatable

Stay close to real bug bounty workflows
---

## 🚀 Features

🔍 Subdomain Enumeration
Uses Amass, Subfinder, Sublist3r, DNSrecon

🌐 Live Host Detection
Fast probing via httpx

📜 Real JavaScript Endpoint Extraction
Parses JS files to extract hidden endpoints & params

🧪 Smart Nuclei Scanning
Runs only relevant templates to reduce noise

⚡ Parallel Execution
Faster recon without melting your system

📂 Scope File Support
Stay in scope, always

🔄 Self Update Mechanism
Update ReconX without reinstalling

🎨 Animated ASCII Banner
Clean startup animation — because terminal UX matters

# ⚙️ Installation

1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/reconx.git
cd reconx
```

2️⃣ Make executable
```bash
chmod +x reconx.py
```

3️⃣ Optional: install as system command
```bash
sudo ln -s $(pwd)/reconx.py /usr/local/bin/reconx
```

4️⃣ Install Python dependencies
```bash
pipx install -r requirements.txt
```

5️⃣ Required external tools
```bash
amass subfinder sublist3r dnsrecon httpx nuclei
```
### ▶️ Usage Examples

 Full recon

```bash
reconx -d example.com --all
```

Subdomain enumeration only
```bash
reconx -d example.com --subs
```

Subdomains + live hosts
```bash
reconx -d example.com --subs --live
```

JS + Nuclei scan
```bash
reconx -d example.com --js --nuclei
```

Update ReconX
```bash
reconx --update
```

## 🛠 Troubleshooting

Command not found → Ensure all tools (amass, subfinder, sublist3r, dnsrecon, httpx, nuclei) are installed and in $PATH.

Permission denied → Run chmod +x reconx.py and/or use sudo.

Python dependency issues → Run pip3 install -r requirements.txt.

Missing outputs → Confirm subdomain enumeration completed successfully.

JS / Reflected modules not working → Check network connectivity and target accessibility.
