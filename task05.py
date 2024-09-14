import scapy.all as scapy

def process_packet(packet):
    # Your packet processing code here
    print(packet.summary())

def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

interface = "Wi-Fi"  # Update to the exact name of your interface
print(f"Sniffing packets on interface {interface}...")
sniff_packets(interface)
