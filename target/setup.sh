file="/etc/systemd/system/backdoor.service"
sudo apt update
sudo apt install python3-pip -y
sudo ufw allow 5000
pip3 install -r ./src/requirements.txt
sudo timedatectl set-timezone Europe/Brussels
sudo rm -rf /opt/ex
cp -r ./src /opt/ex
cd ..
rm -rf ./target
cd /opt/ex
sudo chmod 777 ./start.sh
if [ -f "$file" ] ; then
    sudo systemctl stop backdoor.service
    sudo systemctl disable backdoor.service
    rm "$file"
fi
sudo cp ./backdoor.service "$file"
systemctl daemon-reload
sudo systemctl enable backdoor.service
sudo systemctl start backdoor.service