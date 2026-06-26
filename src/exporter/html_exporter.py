"""
HTML Report Exporter
"""

def export_html(report):

    html = f"""

    <html>

    <body>

    <h1>Network Port Scanner Report</h1>

    <pre>{report}</pre>

    </body>

    </html>

    """

    with open("reports/report.html","w") as file:

        file.write(html)
