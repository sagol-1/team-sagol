from scapy.all import *

A_MAC="AA:AA:AA:AA:AA:AA"
D_IP="255.0.1.2"
B_IP="225.0.1.3"
B_MAC="BB:BB:BB:BB:BB:BB"

# Reconstruct packet with decrypted payload bytes to send out
# With updated addresses
def reconstruct_decrypted_pkt(decrypted_payload):
    return Ether(src=A_MAC, dst=B_MAC)/ \
            IP(src=D_IP, dst=B_IP)/ \
                decrypted_payload
                
