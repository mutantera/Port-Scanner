# Port Scanner Tool

This is a Python-based port scanner tool designed to quickly and efficiently scan a range of ports on a target IP address or domain. It leverages the power of the Nmap utility to provide reliable and accurate results.

## Features

- **Fast and Efficient**: Uses multi-threading to scan multiple ports simultaneously.
- **Nmap Integration**: Leverages the robust capabilities of Nmap for scanning, ensuring high accuracy.
- **Customizable Port Range**: Easily modify the port range to scan specific ports of interest.
- **Open Source**: Completely open source and easy to modify or extend.

## Prerequisites

Before running the port scanner, ensure that you have the following installed:

- **Python 3.x**
- **Nmap**: Ensure that Nmap is installed and available in your system's PATH.
- **python-nmap**: Python wrapper for Nmap. You can install it using pip:

  ```bash
  pip install python-nmap
Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/Port-Scanner.git
Navigate to the project directory:

bash
Copy code
cd Port-Scanner
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
If a requirements.txt file is not present, install python-nmap as shown above.

Usage
To run the port scanner, execute the port.py script with Python:

bash
Copy code
python port.py
Customizing the Target and Port Range
Modify the target IP address and port range by editing the port.py script:

python
Copy code
target = '192.168.173.90'  # Replace with the IP address you want to scan
port_range = '1-1024'  # Adjust the port range as needed
After making changes, rerun the script to scan the specified target and port range.

Example Output
plaintext
Copy code
Scanning 192.168.173.90 for open ports in the range 1-1024...
Host: 192.168.173.90 (hostname)
State: up
Protocol: tcp
Port 22 is open
Port 80 is open
Port 443 is open
Open ports: [22, 80, 443]
Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss any changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
