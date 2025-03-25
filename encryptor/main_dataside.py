from scapy.all import *
from tashtiot_utils.check_pkt import check_pkt, INVALID_PKT, VALID_PKT_FROM_RED, VALID_PKT_FROM_BLACK
from tashtiot_utils.get_payload_to_encrypt import get_payload_to_encrypt
from tashtiot_utils.get_payload_to_decrypt import get_payload_to_decrypt
from tashtiot_utils.reconstruct_encrypted_pkt import reconstruct_encrypted_pkt
from tashtiot_utils.reconstruct_decrypted_pkt import reconstruct_decrypted_pkt
from Matzpin import encryptor, decryptor

red_machine_ip = "10.0.0.1"
black_machine_ip = "10.0.0.2"

# Example of two-way packet handling
def process_packet(pkt):
    pkt_status = check_pkt(pkt, red_machine_ip, black_machine_ip)

    # If packet is invalid/irrelevant, ignore it
    if pkt_status == INVALID_PKT:
        return
    # If packet from red network/machine, we need to encrypt it and send to black network/machine
    elif pkt_status == VALID_PKT_FROM_RED:
        payload_to_encrypt = get_payload_to_encrypt(pkt) # Extract portion we want to encrypt
        encrypted_payload = encryptor(payload_to_encrypt) # Encrypt it
        outgoing_pkt = reconstruct_encrypted_pkt(encrypted_payload) # Build new packet with encrypted payload
    # Otherwise, it came from black network/computer and we need to decrypt it and send to red
    else: 
        payload_to_decrypt = get_payload_to_decrypt(pkt) # Get encrypted portion of packet
        decrypted_payload = decryptor(payload_to_decrypt) # Decrypt it
        outgoing_pkt = reconstruct_decrypted_pkt(decrypted_payload) # Construct full valid decrypted packet to send
    
    # Send new packet on layer 3
    return outgoing_pkt
    # send(outgoing_pkt)

# Monitor interface for traffic and handle each packet
# sniff(prn=process_packet)
