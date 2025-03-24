from scapy.all import *

packet = Ether(src="00:B0:D0:63:C2:26", dst="ff:ff:ff:ff:ff:ff")/ \
            IP(src="12.0.0.1", dst="196.168.1.100")/ \
            TCP(sport=20, dport=80)/ Raw(load="Hello World!")

print(packet.summary())
print(packet.show())

print("Hooray! Your environment is (probably) ready!")