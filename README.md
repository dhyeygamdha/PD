# PD Recon Orchestrator

A **cross-platform Python** script to automate installation and execution of ProjectDiscovery reconnaissance tools:

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

```bash
# Clone the repo (or download pd_enum_installer.py directly)
git clone https://github.com/SnB0y/pd.git
cd pd 

# Make the script executable
chmod +x pd.py
