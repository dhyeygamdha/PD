#!/usr/bin/env python3
"""
Cross-platform installer and enumeration script for ProjectDiscovery tools:
- subfinder      (plain host list)
- httpx          (live HTTP hosts)
- urlfinder      (URL extraction)
- nuclei         (vulnerability scanning)

Features:
1. Installs Go (if missing) and ProjectDiscovery tools + nuclei-templates
2. Automatically adds your Go bin folder (GOPATH/bin) to PATH at runtime
3. Takes a main domain (or file of domains) as input
4. Runs: subfinder → httpx → urlfinder → nuclei
5. Outputs plain-text results per tool in output/<domain>/
"""

import os
import sys
import subprocess
import argparse
import platform
import shutil

# ProjectDiscovery tools for installation
tools = {
    'subfinder':   'github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest',
    'httpx':       'github.com/projectdiscovery/httpx/cmd/httpx@latest',
    'urlfinder':   'github.com/projectdiscovery/urlfinder/cmd/urlfinder@latest',
    'nuclei':      'github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest'
}

def print_banner():
    banner = r"""
  _____  _____                   _               _               
 |  __ \|  __ \                 | |             | |              
 | |__) | |  | |   ___  _ __ ___| |__   ___  ___| |_ _ __ __ _   
 |  ___/| |  | |  / _ \| '__/ __| '_ \ / _ \/ __| __| '__/ _` |  
 | |    | |__| | | (_) | | | (__| | | |  __/\__ \ |_| | | (_| |  
 |_|    |_____/   \___/|_|  \___|_| |_|\___||___/\__|_|  \__,_|  

    by sinb0y
    """
    print(banner)


def run(cmd, **kwargs):
    print(f"[+] Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True, **kwargs)


def add_gobin_to_path():
    try:
        gobin = subprocess.check_output(['go', 'env', 'GOPATH'], stderr=subprocess.DEVNULL).decode().strip()
        binpath = os.path.join(gobin, 'bin')
        if os.path.isdir(binpath):
            os.environ['PATH'] = binpath + os.pathsep + os.environ.get('PATH', '')
    except Exception:
        pass


def install_go_linux():
    GO_VERSION = '1.20.5'
    url = f'https://golang.org/dl/go{GO_VERSION}.linux-amd64.tar.gz'
    run(['curl', '-LO', url])
    run(['sudo', 'rm', '-rf', '/usr/local/go'])
    run(['sudo', 'tar', '-C', '/usr/local', '-xzf', f'go{GO_VERSION}.linux-amd64.tar.gz'])
    os.environ['PATH'] = '/usr/local/go/bin:' + os.environ.get('PATH', '')


def install_go_windows():
    run(['choco', 'install', 'golang', '-y'])
    for p in [r"C:\Program Files\Go\bin", r"C:\Program Files (x86)\Go\bin"]:
        if os.path.isdir(p):
            os.environ['PATH'] = p + os.pathsep + os.environ.get('PATH', '')
    add_gobin_to_path()
    try:
        subprocess.run(['go', 'version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        print("[!] 'go' still not found after installation. Please restart your shell or add Go to PATH.")
        sys.exit(1)


def install_pd_tools():
    try:
        subprocess.run(['go', 'version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        os_type = platform.system().lower()
        if os_type == 'linux':
            install_go_linux()
        elif os_type == 'windows':
            install_go_windows()
        else:
            print(f"[!] Unsupported OS for auto-install: {os_type}")
            sys.exit(1)

    for name, path in tools.items():
        run(['go', 'install', path])

    add_gobin_to_path()
    run(['nuclei', '-update-templates'])
    add_gobin_to_path()
    print("[✔] ProjectDiscovery tools + nuclei-templates installed. Ready to enumerate.")


def enumerate_domain(domain):
    out_dir = os.path.join('output', domain)
    os.makedirs(out_dir, exist_ok=True)

    sf_txt = os.path.join(out_dir, 'subfinder.txt')
    run(['subfinder', '-d', domain, '-silent', '-o', sf_txt])

    http_txt = os.path.join(out_dir, 'httpx.txt')
    run(['httpx', '-l', sf_txt, '-silent', '-o', http_txt])

    urlfinder_txt = os.path.join(out_dir, 'urlfinder.txt')
    run(['urlfinder', '-l', sf_txt, '-silent', '-o', urlfinder_txt])

    nuclei_txt = os.path.join(out_dir, 'nuclei.txt')
    run(['nuclei', '-l', sf_txt, '-silent', '-o', nuclei_txt])

    print(f"[✔] Done for {domain}:")
    print(f"  • Hosts list:   {sf_txt}")
    print(f"  • HTTP live:    {http_txt}")
    print(f"  • URLs found:   {urlfinder_txt}")
    print(f"  • Nuclei scan:  {nuclei_txt}")


def main():
    # Print description and banner each run
    print(__doc__)
    print_banner()

    parser = argparse.ArgumentParser(
        description='Install & run PD enumeration (subfinder → httpx → urlfinder → nuclei)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--install-tools', action='store_true', help='Install Go & PD tools + templates')
    group.add_argument('--domain',     help='Single domain to enumerate')
    group.add_argument('--domains',    help='File with list of domains')
    args = parser.parse_args()

    if args.install_tools:
        install_pd_tools()
        return

    add_gobin_to_path()

    missing = [t for t in tools if not shutil.which(t)]
    if missing:
        print(f"[!] Missing tools: {', '.join(missing)}. Run with --install-tools first.")
        sys.exit(1)

    if args.domain:
        enumerate_domain(args.domain)
    else:
        with open(args.domains, 'r') as f:
            for line in f:
                dom = line.strip()
                if dom:
                    enumerate_domain(dom)

if __name__ == '__main__':
    main()
