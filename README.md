# ReconX 🔎  
### A Personal Reconnaissance Framework for Bug Bounty

    "██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗\n"
    "██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝\n"
    "██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ \n"
    "██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ \n"
    "██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗\n"
    "╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝\n"

    
**A personal recon framework I built while hunting bugs and reading JavaScript.**  
**Built with love & code by Purushotham R**  
**Reconnaissance Framework for Bug Bounty**

---

## 🧠 Why ReconX?

Most recon tools either create **too much noise** or hide everything behind automation.  
ReconX was built to stay **close to the workflow of a real bug bounty hunter**.

The goal is simple:

> Reduce repetition.  
> Keep outputs readable.  
> Leave space for manual thinking.

ReconX helps you find **attack surface**, not fake confidence.

---

## 🚀 Features

- 🔍 Subdomain enumeration using:
  - Amass
  - Subfinder
  - Sublist3r
  - DNSrecon
- 🌐 Live host detection using httpx  
- 📜 JavaScript endpoint extraction (real-world parsing)  
- 🧪 Smart Nuclei scanning (low-noise, targeted templates)  
- ⚡ Parallel execution for faster recon  
- 📂 Scope file support  
- 🔎 Reflected parameter detection  
- 📢 Optional Slack / Discord notifications  
- 🕒 Timestamped logs  
- 🎨 Animated ASCII banner in terminal  
- 🔄 Upgradeable & modular design  

---




## ⚙️ Installation

### 1️⃣ Clone the repository


"git clone https://github.com/yourusername/reconx.git
cd reconx "

### 2️⃣ Make the script executable

" chmod +x reconx.py "

### 3️⃣ (Optional) Install as a system command

sudo ln -s $(pwd)/reconx.py /usr/local/bin/reconx

### 4️⃣ Install Python dependencies

" pipx install -r requirements.txt "

### 5️⃣ Required external tools

Make sure these tools are installed and available in your $PATH:

amass
subfinder
sublist3r
dnsrecon
httpx
nuclei
---

▶️ Usage Examples
Full recon
reconx -d example.com --all

Subdomain enumeration only
reconx -d example.com --subs

Subdomains + live hosts
reconx -d example.com --subs --live

JavaScript + Nuclei scan
reconx -d example.com --js --nuclei

Update ReconX
reconx --update

