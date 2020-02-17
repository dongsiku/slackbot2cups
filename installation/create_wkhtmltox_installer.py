import sys
from os import path

"""
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb  # WSL-Debian
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb  # Ubuntu 18.04

sudo dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb
sudo apt install --fix-broken
"""


def create_wkhtmltox_installer():
    if len(sys.argv) == 2:
        installation_dirname = sys.argv[1]
    else:
        installation_dirname = "./"

    print("Input the environment")
    environment_num = int(input(
        "[0] Raspbian, [1] WSL-Debian, [2] Ubuntu 18.04 (Default: 0): "))

    wkhtmltopdf_link = "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/"

    wkhtmltopdf_basename = "wkhtmltox_0.12.5-1.raspbian.stretch_armhf.deb"
    if environment_num == 1:
        wkhtmltopdf_basename = "wkhtmltox_0.12.5-1.stretch_amd64.deb"
    elif environment_num == 2:
        wkhtmltopdf_basename = "wkhtmltox_0.12.5-1.bionic_amd64.deb"

    wkhtmltox_installer_sh_write_lines = [
        "#!/bin/bash",
        "wget -P {} {}".format(installation_dirname, path.join(wkhtmltopdf_link, wkhtmltopdf_basename)),
        "sudo dpkg -i {}".format(path.join(installation_dirname, wkhtmltopdf_basename))
    ]

    with open(path.join(installation_dirname, "wkhtmltox_installer.sh"), "w")\
            as f_wkhtmltox_installer_sh:
        for line in wkhtmltox_installer_sh_write_lines:
            f_wkhtmltox_installer_sh.write("{}\n".format(line))


if __name__ == "__main__":
    create_wkhtmltox_installer()
