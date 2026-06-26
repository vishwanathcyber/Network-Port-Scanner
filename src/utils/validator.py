"""
Input Validator
"""

def validate_port(port):

    return 1 <= port <= 65535


def validate_host(host):

    return len(host.strip()) > 0
