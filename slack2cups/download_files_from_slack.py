import requests
import codecs
from os import path
from pathlib import Path

from slackbot_settings import slack_token


def download_files_from_slack(url_private_download, download_dirname="./"):
    download_dir = Path(download_dirname)
    download_dir.mkdir(exist_ok=True)  # For debug

    save_file_basename = path.basename(url_private_download)
    save_file_filename = path.join(download_dirname, save_file_basename)

    content = requests.get(
        url_private_download, allow_redirects=True, headers={
            'Authorization': 'Bearer {API_TOKEN}'.format(
                API_TOKEN=slack_token)}, stream=True).content

    save_file = codecs.open(save_file_filename, 'wb')
    save_file.write(content)
    save_file.close()

    return save_file_filename


if __name__ == "__main__":
    from test_variable import sample_url_private_download
    download_files_from_slack(sample_url_private_download)
