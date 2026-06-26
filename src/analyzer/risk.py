"""
Risk Classification
"""

HIGH_RISK_PORTS = [

    21,

    23,

    445,

    3389

]

def classify(port):

    if port in HIGH_RISK_PORTS:

        return "High"

    return "Low"
