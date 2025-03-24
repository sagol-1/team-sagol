from scapy.all import *

# Extract encrypted payload from packet to decrypt as bytes/string. 
# Note: Logic depends on which headers were encrypted too
def get_payload_to_decrypt(pkt):
    return "Hi! I'm a placeholder payload :)"
