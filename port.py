import os
import nmap

# Manually add Nmap's installation directory to the PATH
os.environ['PATH'] += r";C:\Program Files (x86)\Nmap"  # Adjust this path as necessary

# Initialize the Nmap PortScanner
nm = nmap.PortScanner()

# Target IP address or domain
target = '192.168.173.90'

# Port range to scan
port_range = '1-511'

# Run the scan
print(f"Scanning {target} for open ports in the range {port_range}...")

nm.scan(target, port_range, arguments='-sS')

# Retrieve scan results
print(f"Host: {target} ({nm[target].hostname()})")
print(f"State: {nm[target].state()}")

# Iterate over all detected open ports
open_ports = []
for protocol in nm[target].all_protocols():
    print(f"Protocol: {protocol}")
    ports = nm[target][protocol].keys()
    for port in ports:
        if nm[target][protocol][port]['state'] == 'open':
            print(f"Port {port} is open")
            open_ports.append(port)

print(f"Open ports: {open_ports}")
