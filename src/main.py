"""
Network Port Scanner

Main application entry point.
"""

from scanner.tcp_scanner import scan_port

def main():

    print("=" * 60)
    print("Network Port Scanner")
    print("=" * 60)

    host = input("Target IP or Hostname: ")

    port = int(input("Port: "))

    scan_port(host, port)

if name == "main":
    main()
