from scapy.all import *

SRC_IP="255.0.1.2"
DST_IP="225.0.1.3"

# Reconstruct packet with decrypted payload bytes to send out
# With updated addresses
def reconstruct_decrypted_pkt(decrypted_payload):
    return Ether() / \
            IP(src=SRC_IP, dst=DST_IP)/ \
                scapy.layers.inet.TCP(decrypted_payload)
                