from scapy.all import *

SRC_IP="10.0.0.2"
DST_IP="255.0.1.2"

# Reconstruct packet with new encrypted payload bytes to send out
# With updated addresses
def reconstruct_encrypted_pkt(encrypted_payload):
    return Ether()/ \
            IP(src=SRC_IP, dst=DST_IP)/ \
                encrypted_payload
