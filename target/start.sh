sudo apt update
sudo apt install python3-pip -y
sudo ufw allow 5000
pip3 install -r ./src/requirements.txt
sudo timedatectl set-timezone Europe/Brussels
cd src
sudo nohup python3 main.py &