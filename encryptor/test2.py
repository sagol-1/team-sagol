from scapy.all import *
from main_dataside import process_packet

A_MAC="AA:AA:AA:AA:AA:AA"
A_IP="10.0.0.1"

C_MAC="CC:CC:CC:CC:CC:CC"
C_IP="10.0.0.2"

D_MAC="DD:DD:DD:DD:DD:DD"
D_IP="255.0.1.2"

B_MAC="BB:BB:BB:BB:BB:BB"
B_IP="225.0.1.3"

packet = Ether(src=A_MAC, dst=B_MAC)/ \
            IP(src=A_IP, dst=C_IP)/ \
            TCP(sport=20, dport=80)/ \
                Raw(load="CHECK IF its WORKS PLEASE!")

print(" ================================== BEFORE ENCRYPT ================================== ")
print(packet.show())
print(" ================================== AFTER ENCRYPT ================================== ")
outgoing_pkt = process_packet(packet)
print(outgoing_pkt.show())
print(" ================================== AFTER DECRYPT ================================== ")
decrypt_pkt = process_packet(outgoing_pkt)
print(decrypt_pkt.show())
print(" ================================== FINISHED ================================== ")


