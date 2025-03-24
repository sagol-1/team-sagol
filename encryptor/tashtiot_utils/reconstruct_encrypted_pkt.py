from scapy.all import *

A_MAC="AA:AA:AA:AA:AA:AA"
C_IP="10.0.0.2"
D_IP="255.0.1.2"
B_MAC="BB:BB:BB:BB:BB:BB"

# Reconstruct packet with new encrypted payload bytes to send out
# With updated addresses
def reconstruct_encrypted_pkt(encrypted_payload):
    return Ether(src=A_MAC, dst=B_MAC)/ \
            IP(src=C_IP, dst=D_IP)/ \
                encrypted_payload
                

