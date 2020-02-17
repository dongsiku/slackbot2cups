#!/bin/bash

INSTALL_SH_FILENAME=`readlink -f $0`
INSTALL_SH_DIRNAME=`dirname $INSTALL_SH_FILENAME`
PROJECT_DIRNAME=`dirname $INSTALL_SH_DIRNAME`

# Install wkhtmltopdf
python3 $INSTALL_SH_DIRNAME/create_wkhtmltox_installer.py $INSTALL_SH_DIRNAME
bash $INSTALL_SH_DIRNAME/wkhtmltox_installer.sh
sudo apt install --fix-broken

# Install Fonts
sudo apt install fonts-noto-cjk

# Create venv and Install pip
python3 -m venv $PROJECT_DIRNAME/.env
$PROJECT_DIRNAME/.env/bin/pip3 install -U pip
$PROJECT_DIRNAME/.env/bin/pip3 install -r $PROJECT_DIRNAME/requirements.txt


# Create service
echo "[Unit]" > $INSTALL_SH_DIRNAME/slackbot2cups.service
echo "Description = slackbot2cups" >> $INSTALL_SH_DIRNAME/slackbot2cups.service
echo "" >> $INSTALL_SH_DIRNAME/slackbot2cups.service

echo "[Service]" >> $INSTALL_SH_DIRNAME/slackbot2cups.service
echo "ExecStart = $PROJECT_DIRNAME/.env/bin/python3 $PROJECT_DIRNAME/run.py" >> $INSTALL_SH_DIRNAME/slackbot2cups.service
echo "Restart = no" >> $INSTALL_SH_DIRNAME/slackbot2cups.service
echo "Type = simple" >> $INSTALL_SH_DIRNAME/slackbot2cups.service
echo "" >> $INSTALL_SH_DIRNAME/slackbot2cups.service

echo "[Install]" >> $INSTALL_SH_DIRNAME/slackbot2cups.service
echo "WantedBy = multi-user.target" >> $INSTALL_SH_DIRNAME/slackbot2cups.service

#sudo cp $INSTALL_SH_DIRNAME/slackbot2cups.service /etc/systemd/system/slackbot2cups.service
#sudo systemctl enable slackbot2cups
#sudo systemctl start slackbot2cups 
