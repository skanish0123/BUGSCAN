# BUGSCAN - Advanced Security Tool
# Developer: ANISH
# pip install bugscan-tool

import socket
import os
import sys
import platform

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
{Y}║{C}       🛡️  BUGSCAN SECURITY TOOLKIT v2.0  🛡️{Y}           ║
{Y}╚══════════════════════════════════════════════════════╝{RESET}
""")

def menu():
    print(f"""{C}
┌──────────────────────────────────────────────────┐
│                 {Y}📌 MAIN MENU {C}                   │
├──────────────────────────────────────────────────┤
│  {G}1.{RESET} {W}HOST SCANNER{RESET}                           │
│  {G}2.{RESET} {W}SUBFINDER{RESET}                             │
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

def host_scanner():
    host = input(f"{Y}[?] Enter Host/IP {W}» {RESET}")
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    if response == 0:
        print(f"{G}[✓] Host {host} is UP{RESET}")
    else:
        print(f"{R}[✗] Host {host} is DOWN{RESET}")

def subfinder():
    domain = input(f"{Y}[?] Enter Domain {W}» {RESET}")
    print(f"{C}[*] Finding subdomains for {domain}{RESET}")
    print(f"{Y}[!] Install: go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest{RESET}")

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
    print(f"{G}[✓] BUGSCAN v2.0 is up to date{RESET}")

def show_help():
    print(f"""{C}
┌────────────────────────────────────────────────┐
│ {BOLD}HELP SECTION{RESET}{C}                              │
├────────────────────────────────────────────────┤
│ 1. Host Scanner - Ping test                    │
│ 2. Subfinder - Find subdomains (external)      │
│ 3. IP Lookup - Resolve domain to IP            │
│ 4. File Toolkit - Read/Write/Delete files      │
│ 5. Port Scanner - TCP port scan                │
│ 6. DNS Record - Get DNS information            │
│ 7. Host Info - System & network info           │
│ 8. Help - Show this menu                       │
│ 9. Update - Check for updates                  │
│ 0. Exit - Close BUGSCAN                        │
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
            subfinder()
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