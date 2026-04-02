import sys
import os
from scapy.all import Ether, ARP, srp
from rich import print
import pyfiglet

def check_privileges():
    """Check if the script is running with root/administrator privileges."""
    # os.geteuid() works on Linux/Unix. 
    # For a cross-platform script, we handle the check gracefully.
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    
    if not is_admin:
        print("[bold red][!] Error: This tool requires Root/Administrator privileges to send raw packets.[/bold red]")
        print("[bold yellow]Please run the script using 'sudo python main.py' or as Administrator.[/bold yellow]")
        sys.exit(1)

def secure_mind_team_format():
    """Print the professional banner for SecureMind Team."""
    print(f"\n[bold italic white on red]{'-' * 30} Live Host Machine {'-' * 30}[/]")
    print("[blue]*[/blue]" * 79)
    print(pyfiglet.figlet_format("SecureMind Team", justify="center"))
    print("[blue]*[/blue]" * 79)

def scan_network(ip_dst):
    """Send ARP requests and print responding hosts."""
    bc_mac = 'ff:ff:ff:ff:ff:ff'
    
    # Crafting the packet
    ether_header = Ether(dst=bc_mac)
    ether_arp = ARP(pdst=ip_dst)
    arp_packet = ether_header / ether_arp
    
    print(f"\n[bold green][*] Scanning {ip_dst} ... Please wait.[/bold green]\n")
    
    # Sending the packet (verbose=False keeps the terminal clean)
    receive, not_receive = srp(arp_packet, timeout=2, verbose=False)
    
    # Parsing and printing responses
    if not receive:
        print("[bold yellow][!] No active hosts found or check your network connection.[/bold yellow]")
    else:
        for snd, rcv in receive:
            print(f"[*] src Ip Is > [bold cyan]{rcv[Ether].psrc:<15}[/bold cyan] src Mac Is > [bold red]{rcv[Ether].hwsrc}[/bold red]")
    print("\n")

def main():
    # 1. Check permissions first
    check_privileges()
    
    # 2. Print Banner
    secure_mind_team_format()
    
    # 3. Get User Input & Run Scan safely
    try:
        ip_dst = input("Enter destination IP address (e.g., 192.168.1.1/24): ")
        if ip_dst.strip():
            scan_network(ip_dst)
        else:
            print("[bold red][!] Invalid input. IP address cannot be empty.[/bold red]")
            
    except KeyboardInterrupt:
        print("\n[bold yellow][!] Scan interrupted by user. Exiting gracefully...[/bold yellow]")
        sys.exit(0)
    except Exception as e:
        print(f"\n[bold red][!] An unexpected error occurred: {e}[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
