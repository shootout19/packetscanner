# Packet Scanner Script

## **Overview**
This script checks the first 1000 ports of a target IP address to find out which ones are open. It uses Python's built-in socket library to make connections and detect open ports. It's a helpful tool for learning about port scanning and network security basics.

## **Features**
- Scans the first 1000 ports of a target IP.
- Identifies open ports and displays them.
- Simple and beginner-friendly code.

## **Setup and Usage**
1. Clone this repository:
   ```bash
   git clone https://github.com/shootout19/packetscanner.git
   cd packetscanner
2. Open the script (`packetscanner.py`) and replace the `target_IP` variable with the IP address you want to scan
3. Run the script:
   ```bash
   python packetscanner.py
4. The script will display the open ports for given target IP.
