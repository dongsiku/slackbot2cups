from os import path
from pathlib import Path

from .text2pdf import text2pdf

# import image2pdf
from .download_files_from_slack import download_files_from_slack

from .pdf2cups import pdf2cups


class Slack2Cups:
    def __init__(self, project_dirname):
        self.downloads_dirname = path.join(project_dirname, "downloads")
        download_dir = Path(self.downloads_dirname)
        download_dir.mkdir(exist_ok=True)

    def link2cups(self, link):
        downloaded_filename = \
            download_files_from_slack(link, self.downloads_dirname)

        extension = downloaded_filename.rsplit(".", 1)[-1]

        if extension == "pdf":
            pdf2cups(downloaded_filename)
        elif is_imagefile(extension):
            pdf2cups(downloaded_filename)

    def text2pdf(self, text):
        pdf_filename = text2pdf(text, self.downloads_dirname)
        pdf2cups(pdf_filename)


def is_imagefile(extension):
    imagefile_extensions = ["jpeg", "jpg", "png"]
    return (extension in imagefile_extensions)
