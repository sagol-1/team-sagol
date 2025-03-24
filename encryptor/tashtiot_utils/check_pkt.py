from scapy.all import *

VALID_PKT_FROM_RED = 0
VALID_PKT_FROM_BLACK = 1
INVALID_PKT = -1

# Check if incoming packet is valid and if it's coming from red or black network
# For example: check existance of IP header, if source IP is known...
def check_pkt(pkt, red_machine_ip, black_machine_ip):
    return INVALID_PKT
