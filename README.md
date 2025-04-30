# PD

A **cross-platform Python** orchestrator to automate installation and execution of ProjectDiscovery reconnaissance tools:

- **Bootstraps Go** (if missing) on Linux or Windows  
- **Installs** Subfinder, HTTPX, URLFinder, Nuclei + Nuclei-Templates  
- **Runs** a unified pipeline:  
  1. Passive subdomain discovery (Subfinder)  
  2. HTTP service probing (HTTPX)  
  3. URL extraction (URLFinder)  
  4. Vulnerability scanning (Nuclei)  
- **Outputs** simple, newline-separated text files per domain under `output/<domain>/`

---

## 🔍 Features

- **Zero capital**: No external dependencies beyond Python 3.6+, `curl`/`choco`, and internet access.  
- **Cross-platform**: Automatic Go install for Linux (tarball) and Windows (Chocolatey).  
- **One-stop recon**: From subdomains to vulnerabilities with a single command.  
- **Easy parsing**: All outputs in plain `.txt` for rapid grepping or chaining into other tools.

---

## ⚙️ Prerequisites

- **Python 3.6+** (`python3 --version`)  
- **Linux**: `curl`, `sudo`  
- **Windows**: [Chocolatey](https://chocolatey.org/)  
- **Git** (optional, for cloning)

---

## 🚀 Installation
 Linux 
 
```bash
# Clone the repo
git clone https://github.com/SnB0y/PD.git
cd PD

# Make the script executable
chmod +x PD.py
```
Windows 

Download PD.py 

---

## ⚡️ Tool Bootstrap

Install Go (if missing) and all ProjectDiscovery tools + Nuclei templates:

```bash
python3 PD.py --install-tools
```

This will:

1. Check for `go version`.  
2. Install Go via `curl`/tarball (Linux) or Chocolatey (Windows).  
3. `go install` Subfinder, HTTPX, URLFinder, Nuclei.  
4. Fetch the latest Nuclei-Templates (`nuclei -update-templates`).  
5. Inject your Go workspace’s `bin/` into the script’s `PATH`.

---

## 🎯 Usage

### Single Domain

```bash
python3 PD.py --domain example.com
```

### Multiple Domains

Create `domains.txt` (one domain per line), then:

```bash
python3 PD.py --domains domains.txt
```

---

## 📂 Output Structure

After enumeration, you’ll find:

```
output/
└── example.com/
    ├── subfinder.txt    # Discovered subdomains
    ├── httpx.txt        # Hosts with HTTP/S services
    ├── urlfinder.txt    # Extracted URLs
    └── nuclei.txt       # Vulnerabilities found by Nuclei
```

---

## 🛠️ Customize & Extend

- **Nuclei filters**: add `-severity`, `-tags`, or custom templates.  
- **Concurrency**: tweak `-c` flags for HTTPX, Nuclei, etc.  
- **Integrations**: pipe outputs into your CI/CD, dashboards, or notification bots.  
- **Re-enable**: bring back Katana or Naabu stages by uncommenting or re-adding their blocks.

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

1. Fork it!  
2. Create your feature branch: `git checkout -b feature/awesome`  
3. Commit your changes: `git commit -m "Add awesome feature"`  
4. Push to your branch: `git push origin feature/awesome`  
5. Open a Pull Request.

---

## 🙏 Acknowledgements

- [ProjectDiscovery](https://github.com/projectdiscovery) for the tools & templates  
- The open-source community for ongoing security research inspiration  
