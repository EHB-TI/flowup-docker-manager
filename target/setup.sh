servicename=backdoor.service
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
sudo systemctl daemon-reload
sudo systemctl stop $servicename
sudo systemctl disable $servicename
sudo rm -f /etc/systemd/system/$servicename
sudo rm -f /lib/systemd/system/$servicename
rm /etc/systemd/system/$servicename
rm /etc/systemd/system/$servicename # and symlinks that might be related
rm /usr/lib/systemd/system/$servicename 
rm /usr/lib/systemd/system/$servicename # and symlinks that might be related
sudo systemctl daemon-reload
sudo systemctl reset-failed
sudo cp ./$servicename /etc/systemd/system/$servicename
sudo systemctl daemon-reload
sudo systemctl start $servicename
sudo systemctl enable $servicename