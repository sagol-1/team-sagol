from scapy.all import *
from decryptor import decryptor

SRC_MAC = "00:B0:D0:63:C2:26"
DST_MAC = "ff:ff:ff:ff:ff:ff"

SRC_IP = "12.0.0.1"
DST_IP = "196.168.1.100"

# Reconstruct packet with new encrypted payload bytes to send out
# With updated addresses
def reconstruct_encrypted_pkt(encrypted_payload):
    pkt = Ether(src = SCR_IP, dst=DST_IP) / IP(src = SRC_IP, dst=DST_IP) / encrypted_payload # Create packet with encrypted payload
    pkt[Raw].load = encrypted_payload # Update payload
    return pkt
