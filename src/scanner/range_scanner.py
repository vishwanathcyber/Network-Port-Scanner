"""
Port Range Scanner
"""

from scanner.tcp_scanner import scan_port

def scan_range(host, start_port, end_port):

    for port in range(start_port, end_port + 1):

        scan_port(host, port)
