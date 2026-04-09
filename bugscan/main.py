#!/usr/bin/env python3
# BUGSCAN - Advanced Security Toolkit with Subfinder
# Developer: ANISH

import socket
import os
import sys
import platform
import subprocess

R = '\033[91m'; G = '\033[92m'; Y = '\033[93m'; C = '\033[96m'
W = '\033[97m'; RESET = '\033[0m'; BOLD = '\033[1m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{BOLD}{R}
╔══════════════════════════════════════════════════════╗
{R}║{C}   ██████╗ ██╗   ██╗ ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗{R}║
{R}║{C}   ██╔══██╗██║   ██║██╔════╝ ██╔════╝██╔════╝██╔══██╗████╗  ██║{R}║
{R}║{C}   ██████╔╝██║   ██║██║  ███╗███████╗██║     ███████║██╔██╗ ██║{R}║
{R}║{C}   ██╔══██╗██║   ██║██║   ██║╚════██║██║     ██╔══██║██║╚██╗██║{R}║
{R}║{C}   ██████╔╝╚██████╔╝╚██████╔╝███████║╚██████╗██║  ██║██║ ╚████║{R}║
{R}║{C}   ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝{R}║
{R}╚══════════════════════════════════════════════════════╝{RESET}
{BOLD}{Y}╔══════════════════════════════════════════════════════╗
{Y}║{G}         🔥 DEVELOPER: {BOLD}{W}ANISH{RESET}{BOLD}{G} 🔥                    {Y}║
{Y}║{C}       🛡️  BUGSCAN SECURITY TOOLKIT v3.0  🛡️{Y}           ║
{Y}║{C}       🔧 SUBFINDER INTEGRATED 🔧{Y}                       ║
{Y}╚══════════════════════════════════════════════════════╝{RESET}
""")

def menu():
    print(f"""{C}
┌──────────────────────────────────────────────────┐
│                 {Y}📌 MAIN MENU {C}                   │
├──────────────────────────────────────────────────┤
│  {G}1.{RESET} {W}HOST SCANNER{RESET}                           │
│  {G}2.{RESET} {W}SUBFINDER {C}[SUBSCAN]{RESET}                    │
│  {G}3.{RESET} {W}IP LOOKUP{RESET}                             │
│  {G}4.{RESET} {W}FILE TOOLKIT{RESET}                          │
│  {G}5.{RESET} {W}PORT SCANNER{RESET}                          │
│  {G}6.{RESET} {W}DNS RECORD{RESET}                            │
│  {G}7.{RESET} {W}HOST INFO{RESET}                             │
│  {G}8.{RESET} {W}HELP{RESET}                                 │
│  {G}9.{RESET} {W}UPDATE{RESET}                               │
│  {G}0.{RESET} {R}EXIT{RESET}                                 │
└──────────────────────────────────────────────────┘
""")

def check_subfinder():
    """Check if subfinder is installed"""
    result = subprocess.run(["which", "subfinder"], capture_output=True, text=True)
    return result.returncode == 0

def install_subfinder():
    """Install subfinder automatically"""
    print(f"{Y}[!] Subfinder not found! Installing...{RESET}")
    
    # Check if Go is installed
    go_check = subprocess.run(["which", "go"], capture_output=True, text=True)
    if go_check.returncode != 0:
        print(f"{Y}[!] Installing Go first...{RESET}")
        os.system("pkg install golang -y")
    
    # Install subfinder
    print(f"{C}[*] Installing Subfinder via go...{RESET}")
    os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
    
    # Add to path
    os.system("echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc")
    os.system("export PATH=$PATH:$HOME/go/bin")
    
    print(f"{G}[✓] Subfinder installed successfully!{RESET}")
    print(f"{Y}[!] Please restart Termux or run: source ~/.bashrc{RESET}")

def subfinder_tool():
    """Run subfinder on target domain"""
    domain = input(f"{Y}[?] Enter Target Domain {W}» {RESET}")
    
    if not domain:
        print(f"{R}[✗] Domain required!{RESET}")
        return
    
    # Check if subfinder is installed
    if not check_subfinder():
        print(f"{Y}[!] Subfinder not detected{RESET}")
        install = input(f"{Y}[?] Install Subfinder now? (y/n) {W}» {RESET}")
        if install.lower() == 'y':
            install_subfinder()
            print(f"{Y}[!] Please restart the tool after installation{RESET}")
            return
        else:
            print(f"{R}[✗] Subfinder required for this feature{RESET}")
            return
    
    print(f"{C}[*] Scanning subdomains for {domain}...{RESET}")
    print(f"{Y}[+] This may take a few moments{RESET}")
    
    # Run subfinder
    output_file = f"subdomains_{domain}.txt"
    cmd = f"subfinder -d {domain} -silent -o {output_file}"
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        
        # Count and display results
        with open(output_file, 'r') as f:
            subdomains = f.readlines()
        
        if subdomains:
            print(f"{G}[✓] Found {len(subdomains)} subdomains!{RESET}")
            print(f"{C}┌─── SUBDOMAINS ───┐{RESET}")
            for sub in subdomains[:20]:  # Show first 20
                print(f"{G}[+] {sub.strip()}{RESET}")
            if len(subdomains) > 20:
                print(f"{Y}[!] ... and {len(subdomains)-20} more{RESET}")
            print(f"{G}[✓] Saved to: {output_file}{RESET}")
        else:
            print(f"{R}[✗] No subdomains found{RESET}")
            
    except subprocess.CalledProcessError:
        print(f"{R}[✗] Subfinder scan failed!{RESET}")

def host_scanner():
    host = input(f"{Y}[?] Enter Host/IP {W}» {RESET}")
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    if response == 0:
        print(f"{G}[✓] Host {host} is UP{RESET}")
    else:
        print(f"{R}[✗] Host {host} is DOWN{RESET}")

def ip_lookup():
    host = input(f"{Y}[?] Enter Hostname {W}» {RESET}")
    try:
        ip = socket.gethostbyname(host)
        print(f"{G}[✓] IP Address: {W}{ip}{RESET}")
    except:
        print(f"{R}[✗] Failed to resolve{RESET}")

def file_toolkit():
    print(f"{C}┌─── FILE TOOLKIT ───┐{RESET}")
    print(f"{G}1. Read File\n2. Write File\n3. Delete File{RESET}")
    opt = input(f"{Y}[?] Choice {W}» {RESET}")
    fname = input(f"{Y}[?] Filename {W}» {RESET}")
    if opt == "1":
        try:
            with open(fname, 'r') as f:
                print(f"{G}[✓] Content:\n{RESET}{f.read()}")
        except:
            print(f"{R}[✗] Error reading file{RESET}")
    elif opt == "2":
        data = input(f"{Y}[?] Content {W}» {RESET}")
        with open(fname, 'w') as f:
            f.write(data)
        print(f"{G}[✓] File written{RESET}")
    elif opt == "3":
        os.remove(fname)
        print(f"{G}[✓] File deleted{RESET}")

def port_scanner():
    host = input(f"{Y}[?] Target Host {W}» {RESET}")
    ports = input(f"{Y}[?] Ports (comma sep) {W}» {RESET}").split(',')
    print(f"{C}[*] Scanning {host}...{RESET}")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((host, int(port))) == 0:
                print(f"{G}[✓] Port {port} OPEN{RESET}")
            else:
                print(f"{R}[✗] Port {port} CLOSED{RESET}")
            s.close()
        except:
            print(f"{R}[✗] Error on port {port}{RESET}")

def dns_record():
    domain = input(f"{Y}[?] Domain {W}» {RESET}")
    try:
        result = socket.gethostbyname_ex(domain)
        print(f"{G}[✓] DNS Records: {result}{RESET}")
    except:
        print(f"{R}[✗] No records found{RESET}")

def host_info():
    host = input(f"{Y}[?] Host {W}» {RESET}")
    try:
        ip = socket.gethostbyname(host)
        print(f"{C}Hostname: {W}{socket.gethostname()}{RESET}")
        print(f"{C}IP: {W}{ip}{RESET}")
        print(f"{C}System: {W}{platform.system()} {platform.release()}{RESET}")
    except:
        print(f"{R}[✗] Error fetching info{RESET}")

def update_tool():
    print(f"{G}[✓] BUGSCAN v3.0 (Subfinder Integrated){RESET}")
    print(f"{C}[*] Checking for updates...{RESET}")
    os.system("cd BUGSCAN && git pull 2>/dev/null || echo 'Not a git repo'")

def show_help():
    print(f"""{C}
┌────────────────────────────────────────────────┐
│ {BOLD}HELP SECTION{RESET}{C}                              │
├────────────────────────────────────────────────┤
│ {G}2. SUBFINDER{RESET} - Find subdomains (Auto-install) │
│    * Automatically installs Go & Subfinder     │
│    * Saves results to subdomains_*.txt         │
│                                                 │
│ Other tools work as described                  │
└────────────────────────────────────────────────┘
{RESET}""")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(f"{Y}┌─[{G}BUGSCAN{RESET}{Y}]─[{G}ANISH{RESET}{Y}]\n└──» {RESET}")
        
        if choice == "1":
            host_scanner()
        elif choice == "2":
            subfinder_tool()
        elif choice == "3":
            ip_lookup()
        elif choice == "4":
            file_toolkit()
        elif choice == "5":
            port_scanner()
        elif choice == "6":
            dns_record()
        elif choice == "7":
            host_info()
        elif choice == "8":
            show_help()
        elif choice == "9":
            update_tool()
        elif choice == "0":
            print(f"{R}[!] Exiting BUGSCAN...{RESET}")
            sys.exit()
        else:
            print(f"{R}[✗] Invalid choice!{RESET}")
        
        input(f"\n{Y}[!] Press Enter to continue...{RESET}")

def start():
    try:
        ensure_output_dir()
        main()
    except KeyboardInterrupt:
        console.print("\n⚠️ Exiting...")