import pdfkit
from datetime import datetime

from test_variable import sample_text

"""
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb
sudo dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb
sudo apt install --fix-broken
"""


def text2pdf(text):
    # https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
    options = {
        'page-size': 'A4',
        'margin-top': '0.4in',
        'margin-bottom': '0.4in',
        'margin-right': '0.4in',
        'margin-left': '0.4in',
        'encoding': "UTF-8"
    }

    filename = datetime.now().strftime('text_%Y%m%d_%H%M%S')
    html_filename = "{}.html".format(filename)
    pdf_filename = "{}.pdf".format(filename)

    with open(html_filename, "w") as wf:
        wf.write("<!DOCTYPE html>\n")
        wf.write("<html>\n")
        wf.write("<body>\n")
        lines = text.split("\n")
        for line in lines:
            if line != "":
                wf.write("        <p>{}</p>\n".format(line))
        wf.write("    </body>\n")
        wf.write("</html>\n")

    pdfkit.from_file(html_filename, pdf_filename,
                     # css='style.css',
                     options=options)


if __name__ == "__main__":
    text2pdf(sample_text)
