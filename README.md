# NetWatch - Network Traffic Analyzer

A Python-based application for capturing and analyzing network traffic with a web interface.

## Features

- Real-time packet capture using Scapy
- Web-based visualization of network traffic
- Protocol breakdown (TCP/UDP/Others)
- Basic packet details (source/destination, ports, size)
- Responsive web interface

## Requirements

- Python 3.6+
- Scapy (`pip install scapy`)
- Flask (`pip install flask`)
- 
##Instructions (Step-by-Step)
Open CMD as Administrator

Press Win + X → Choose Command Prompt (Admin) or Windows Terminal (Admin)

Run the Command above

It will:

Download the latest Npcap installer (npcap-1.78.exe)

Launch the installer

Wait for you to finish installation

During Installation

Check:

✅ "Install Npcap in WinPcap API-compatible Mode"

(Optional) ✅ Support raw 802.11 traffic for WiFi sniffing

After Installation

Reboot your computer to load the driver properly.
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/netwatch.git

   cd netwatch
