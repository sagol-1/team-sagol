from scapy.all import *
from main_dataside import process_packet

SRC_MAC="AA:AA:AA:AA:AA:AA"
SRC_IP="10.0.0.1"

DST_MAC="CC:CC:CC:CC:CC:CC"
DST_IP="10.0.0.2"

packet = Ether(src=SRC_MAC, dst=DST_MAC)/ \
            IP(src=SRC_IP, dst=DST_IP)/ \
            TCP(sport=20, dport=80)/ Raw(load="CHECK IF its WORKS PLEASE!")

print("====================== BEFORE ENCRYPT ====================== ")
print(packet.show())
print("====================== AFTER ENCRYPT ====================== ")
process_packet(packet)
print(packet.show())
print("====================== AFTER DECRYPT ====================== ")
process_packet(packet)
print(packet.show())
print("====================== FINISHED ====================== ")

# RESULT_SRC_MAC="DD:DD:DD:DD:DD:DD"
# RESULT_SRC_IP="255.0.1.2"

# RESULT_DST_MAC="BB:BB:BB:BB:BB:BB"
# RESULT_DST_IP="255.11.3.2"

