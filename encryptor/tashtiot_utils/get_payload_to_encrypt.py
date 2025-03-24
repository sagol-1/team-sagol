from scapy.all import *

# Extract payload from packet to encrypt as bytes/string. May include higher-layer headers.
def get_payload_to_encrypt(pkt):
    packet = packet[IP].payload
    return bytes(packet)
