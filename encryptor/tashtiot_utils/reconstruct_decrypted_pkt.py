from scapy.all import *
import ast

# Reconstruct packet with decrypted payload bytes to send out
# With updated addresses
def reconstruct_decrypted_pkt(decrypted_payload, SRC_IP, DST_IP):
    decrypted_payload_bytes = ast.literal_eval(decrypted_payload)
    print("+=============================+")
    print(decrypted_payload_bytes)
    print("+=============================+")
    print(type(decrypted_payload_bytes))
    print("+=============================+")
    return Ether()/ \
            IP(src=SRC_IP, dst=DST_IP)/ \
                TCP(decrypted_payload_bytes)