"""
Markdown Report Exporter
"""

def export_markdown(report):

    with open("reports/report.md", "w") as file:

        file.write("# Network Scan Report\n\n")

        file.write(report)
