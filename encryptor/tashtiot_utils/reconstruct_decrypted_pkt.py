# from scapy.all import *

# # Reconstruct packet with decrypted payload bytes to send out
# # With updated addresses
# def reconstruct_decrypted_pkt(decrypted_payload):
#     pkt = Ether(src = "ff:ff:ff:ff:ff:ff", dst="00:B0:D0:63:C2:26") / IP(src = "196.168.1.100", dst="12.0.0.1") / decrypted_payload # Create packet with decrypted payload
#     pkt[Raw].load = decrypted_payload # Update payload
#     return pkt
