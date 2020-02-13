import pdfkit
from datetime import datetime


"""
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb  # WSL-Debian
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb  # Ubuntu 18.04
sudo dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb
sudo apt install --fix-broken
"""


def text2pdf(text, debug_mode=False):
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
    if debug_mode is True:
        html_filename = html_filename.replace(".html", "_temp.html")
        pdf_filename = pdf_filename.replace(".pdf", "_temp.pdf")

    text_html_head_lines = ["<!DOCTYPE html>\n", "<html>\n", "<body>\n"]
    text_html_tail_lines = ["</body>\n", "</html>\n"]

    with open(html_filename, "w") as wf:
        for text_html_head_line in text_html_head_lines:
            wf.write(text_html_head_line)

        lines = text.split("\n")
        for line in lines:
            if line != "":
                wf.write("<p>{}</p>\n".format(line))

        for text_html_tail_line in text_html_tail_lines:
            wf.write(text_html_tail_line)

    pdfkit.from_file(html_filename, pdf_filename,
                     # css='style.css',
                     options=options)


if __name__ == "__main__":
    from test_variable import sample_text
    text2pdf(sample_text, True)
