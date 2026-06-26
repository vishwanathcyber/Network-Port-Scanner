from scanner.tcp_scanner import scan_port

def test_localhost_scan():

    scan_port("127.0.0.1", 80)
