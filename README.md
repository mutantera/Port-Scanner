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
