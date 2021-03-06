import pdfkit
from datetime import datetime
from os import path


"""
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb  # WSL-Debian
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb  # Ubuntu 18.04

sudo dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb
sudo apt install --fix-broken
sudo apt install fonts-noto-cjk  # Fonts
"""


def text2pdf(text, downloads_dirname="./", debug_mode=False):
    # https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
    options = {
        'page-size': 'A4',
        'margin-top': '0.4in',
        'margin-bottom': '0.4in',
        'margin-right': '0.4in',
        'margin-left': '0.4in',
        'encoding': "UTF-8"
    }
    font_size_px = 20

    if debug_mode is True:
        filename = "text_temp"
    else:
        filename = datetime.now().strftime('text_%Y%m%d_%H%M%S')
    html_filename = path.join(downloads_dirname, "{}.html".format(filename))
    pdf_filename = path.join(downloads_dirname, "{}.pdf".format(filename))

    text_html_head_lines = [
        "<!DOCTYPE html>\n",
        "<head>\n",
        '<style type = "text/css">',
        "<!--p {{font-size: {}px;}}--> ".format(font_size_px),
        '</style>',
        "</head>\n",
        "<html>\n",
        "<body>\n"]
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
                     options=options)

    return pdf_filename


if __name__ == "__main__":
    from test_variable import sample_text
    text2pdf(sample_text, debug_mode=True)
