from scapy.all import Ether, ARP, srp
from rich import print
import pyfiglet

bc_mac = 'ff:ff:ff:ff:ff:ff'
ip_dst = input("Enter destination IP address: ")

ether_header = Ether(dst = bc_mac)
ether_arp = ARP(pdst = ip_dst)
arp_packet = ether_header / ether_arp
receive, not_receive= srp(arp_packet, timeout = 2)

#Print Arp Request
def print_request_arp():
    for snd, rcv in receive:
        print(f"src Ip Is > {snd[Ether].psrc}   src Mac Is > {snd[Ether].hwsrc}")
#Print Arp Reply
def print_reply_arp():

    for snd, rcv in receive:
        print(f"src Ip Is > {rcv[Ether].psrc}   src Mac Is > [bold red] {rcv[Ether].hwsrc}")

def secure_mind_team_format():
    print(f"\n[bold italic white on red]{"-" * 30} Live Host Machine {"-" * 30}")
    print("[blue]*" * 79)
    print(pyfiglet.figlet_format("SecureMind Team", justify="center"))
    print("[blue]*" * 79)



secure_mind_team_format()
print_reply_arp()

# --------------------------------------Try Another Way-----------------------------

# ether_header = Ether(dst = bc_mac)
# option_arp = ARP(pdst = ip_dst)
# arp_packet = ether_header / option_arp
#
# result, no_result = srp(arp_packet, timeout = 1, verbose = False)
# for request, reply in result:
#     print(reply.psrc, reply.hwsrc)