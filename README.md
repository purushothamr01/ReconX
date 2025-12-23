# ReconX 🔎
### A Personal Reconnaissance Framework for Bug Bounty

    "██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗\n"
    "██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝\n"
    "██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝ \n"
    "██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗ \n"
    "██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗\n"
    "╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝\n"

    

A personal recon framework I built while hunting bugs, breaking apps, and actually reading JavaScript.
Not a wrapper. Not a copy.
Just the workflow that worked for me — automated, refined, and battle‑tested.

Crafted in terminals, tested on real targets.
Built by Purushotham R

🧠 Why ReconX?

Most recon tools run everything and drown you in noise.
ReconX focuses on signal over volume.

Read JavaScript, don’t ignore it

Scan what matters, not everything

Keep recon fast, clean, and repeatable

Stay close to real bug bounty workflows

🚀 Features

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

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/reconx.git
cd reconx

2️⃣ Install ReconX
pip install .


This installs reconx as a system-wide command.

🔧 Required External Tools

Make sure these are installed and available in your $PATH:

amass
subfinder
sublist3r
dnsrecon
httpx
nuclei


ReconX assumes you know what you’re installing — no bloated auto-installers here.

▶️ Usage Examples
Full Recon
reconx -d example.com --all

Subdomain Enumeration Only
reconx -d example.com --subs

Subdomains + Live Hosts
reconx -d example.com --subs --live

JavaScript Analysis + Nuclei Scan
reconx -d example.com --js --nuclei

Update ReconX
reconx update

🖥️ Screenshots / Demo

📌 Demo GIF coming soon🧠 Why ReconX?

Most recon tools run everything and drown you in noise.
ReconX focuses on signal over volume.

Read JavaScript, don’t ignore it

Scan what matters, not everything

Keep recon fast, clean, and repeatable

Stay close to real bug bounty workflows

🚀 Features

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

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/reconx.git
cd reconx

2️⃣ Install ReconX
pip install .


This installs reconx as a system-wide command.

🔧 Required External Tools

Make sure these are installed and available in your $PATH:

amass
subfinder
sublist3r
dnsrecon
httpx
nuclei


ReconX assumes you know what you’re installing — no bloated auto-installers here.

▶️ Usage Examples
Full Recon
reconx -d example.com --all

Subdomain Enumeration Only
reconx -d example.com --subs

Subdomains + Live Hosts
reconx -d example.com --subs --live

JavaScript Analysis + Nuclei Scan
reconx -d example.com --js --nuclei

Update ReconX
reconx update

🖥️ Screenshots / Demo

📌 Demo GIF coming soon

Troubleshooting

Command not found?

pip show reconx


If not found, reinstall:

pip install .


Tool not detected?
Make sure required binaries are in your $PATH.

Nuclei returns nothing?
Update templates:

nuclei -update-templates

📌 Philosophy

ReconX is not about running more tools.
It’s about running the right ones, at the right time, with intent.

“Most bugs aren’t hidden.
They’re ignored.”

🧩 Roadmap

Auto JS diffing

Param-based attack surface mapping

Smarter recon profiles

Config-based workflows

GitHub Actions support

🤝 Contributing

Pull requests are welcome.
If you’ve got a cleaner workflow or smarter recon logic — let’s build it.

📜 License

MIT License
Use it. Break things. Learn. Share.

⭐ If this helped your recon, give the repo a star.

It tells me the late-night debugging was worth it.

— Purushotham R
