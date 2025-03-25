from scapy.all import *

# Reconstruct packet with decrypted payload bytes to send out
# With updated addresses
def reconstruct_decrypted_pkt(decrypted_payload, SRC_IP, DST_IP):
    return Ether() / \
            IP(src=SRC_IP, dst=DST_IP)/ \
                scapy.layers.inet.TCP(decrypted_payload)
                