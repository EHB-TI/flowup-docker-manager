servicename=backdoor.service
sudo systemctl stop $servicename
sudo systemctl disable $servicename
sudo rm -f /etc/systemd/system/$servicename
sudo rm -f /lib/systemd/system/$servicename
sudo rm -f /etc/systemd/system/$servicename
sudo rm -f /etc/systemd/system/$servicename # and symlinks that might be related
sudo rm -f /usr/lib/systemd/system/$servicename 
sudo rm -f /usr/lib/systemd/system/$servicename # and symlinks that might be related
sudo systemctl daemon-reload
sudo systemctl reset-failed
sudo rm -rf /opt/ex
sudo ufw delete allow 5000