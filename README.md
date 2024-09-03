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
## Installation

Follow these steps to set up the Port Scanner Tool on your local machine:

1. **Clone the Repository**

   Clone this repository to your local machine using Git. Open your terminal or command prompt and run:

   ```bash
   git clone https://github.com/yourusername/Port-Scanner.git
   ```

   This command copies the repository from GitHub to your computer.

2. **Navigate to the Project Directory**

   Change your directory to the project folder:

   ```bash
   cd Port-Scanner
   ```

   This command moves you into the folder containing the project files.

3. **Install Dependencies**

   Install the required Python packages. If a `requirements.txt` file is available, run:

   ```bash
   pip install -r requirements.txt
   ```

   If there is no `requirements.txt` file, you can manually install `python-nmap` with:

   ```bash
   pip install python-nmap
   ```

## Usage

To start using the Port Scanner Tool, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the project directory if you aren’t already there:

   ```bash
   cd Port-Scanner
   ```

3. Run the port scanner script:

   ```bash
   python port.py
   ```

### Customizing the Target and Port Range

You can change the target IP address and port range by editing the `port.py` file. Open `port.py` in a text editor and modify the following lines:

```python
target = '192.168.173.90'  # Replace with the IP address you want to scan
port_range = '1-1024'  # Adjust the port range as needed
```

After updating these values, save the file and run the script again to scan the new target and port range.

## Example Output

When you run the script, you might see output like this:

```plaintext
Scanning 192.168.173.90 for open ports in the range 1-1024...
Host: 192.168.173.90 (hostname)
State: up
Protocol: tcp
Port 22 is open
Port 80 is open
Port 443 is open
Open ports: [22, 80, 443]
```

This output shows the open ports found on the target IP address within the specified range.

## Contributing

We welcome contributions to the Port Scanner Tool! If you have suggestions or improvements, please:

- **Submit a Pull Request**: Propose changes by submitting a pull request on GitHub.
- **Open an Issue**: Report any bugs or request features by opening an issue on GitHub.

## License

This project is licensed under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file in this repository.

## Contact

If you have any questions or need assistance, feel free to contact me at [your email address] or open an issue on GitHub.

Thank you for using the Port Scanner Tool!
```

**Instructions for Customization**:
- **Replace** `yourusername` with your actual GitHub username in the clone URL.
- **Replace** `[your email address]` with your actual contact email.

Feel free to adjust or expand this README as needed!
