"""
Multi-threaded Port Scanner
"""

from concurrent.futures import ThreadPoolExecutor

from scanner.tcp_scanner import scan_port

def threaded_scan(host, ports):

    with ThreadPoolExecutor(max_workers=100) as executor:

        executor.map(lambda port: scan_port(host, port), ports)
