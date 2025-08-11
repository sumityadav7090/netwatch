from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP, Raw
from collections import deque
from datetime import datetime

MAX_PACKETS = 100
packets = deque(maxlen=MAX_PACKETS)

def packet_handler(packet):
    """Process each incoming packet"""
    if IP in packet:
        packet_info = {
            'timestamp': datetime.now().strftime("%H:%M:%S.%f")[:-3],
            'src_ip': packet[IP].src,
            'dst_ip': packet[IP].dst,
            'protocol': packet[IP].proto,
            'size': len(packet),
            'summary': packet.summary()
        }
        
        # Determine the protocol and extract relevant information
        if TCP in packet:
            packet_info['protocol_name'] = 'TCP'
            packet_info['src_port'] = packet[TCP].sport
            packet_info['dst_port'] = packet[TCP].dport
            packet_info['payload'] = str(packet[TCP].payload)[:100]
        elif UDP in packet:
            packet_info['protocol_name'] = 'UDP'
            packet_info['src_port'] = packet[UDP].sport
            packet_info['dst_port'] = packet[UDP].dport
            packet_info['payload'] = str(packet[UDP].payload)[:100]
        elif ICMP in packet:
            packet_info['protocol_name'] = 'ICMP'
            packet_info['payload'] = str(packet[ICMP].payload)[:100]
        elif ARP in packet:
            packet_info['protocol_name'] = 'ARP'
            packet_info['src_mac'] = packet[ARP].psrc
            packet_info['dst_mac'] = packet[ARP].pdst
            packet_info['payload'] = str(packet[ARP].payload)[:100]
        else:
            packet_info['protocol_name'] = 'OTHER'
        
        packets.append(packet_info)

def start_capture(interface=None, filter=None):
    """Start packet capture on specified interface"""
    sniff(prn=packet_handler, store=0, iface=interface, filter=filter)

def get_packets():
    """Return captured packets"""
    return list(packets)
