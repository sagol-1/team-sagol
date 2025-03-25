from scapy.all import *

# Reconstruct packet with new encrypted payload bytes to send out
# With updated addresses
def reconstruct_encrypted_pkt(encrypted_payload, SRC_IP, DST_IP):
    return Ether()/ \
            IP(src=SRC_IP, dst=DST_IP)/ \
                encrypted_payload
                
