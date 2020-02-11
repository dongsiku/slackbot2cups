import requests
import codecs
from os import path
from pathlib import Path

from test_variable import sample_url_private_download
from slackbot_settings import slack_token


def download_files_from_slack(url_private_download):
    download_dir = Path("downloads")
    download_dir.mkdir(exist_ok=True)
    save_file_basename = path.basename(url_private_download)
    save_file_filename = path.join(
        path.dirname(path.abspath(__file__)), "download", save_file_basename)

    content = requests.get(
        url_private_download, allow_redirects=True, headers={
            'Authorization': 'Bearer {API_TOKEN}'.format(
                API_TOKEN=slack_token)}, stream=True).content

    save_file = codecs.open(save_file_filename, 'wb')
    save_file.write(content)
    save_file.close()

    return save_file_basename.split('.', 1)[1]


if __name__ == "__main__":
    download_files_from_slack(sample_url_private_download)
