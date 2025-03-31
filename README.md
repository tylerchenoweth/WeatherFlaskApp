This will pull weather from some API and display it on a webpage. It will also have users.


To install Docker and Docker-Compose on Ubuntu

sudo apt update
sudo apt upgrade
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
docker --version
sudo usermod -aG docker $USER
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.7/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
docker compose up
sudo usermod -aG docker $USER
newgrp docker

sudo reboot



To Run w/o Docker:
* Frontend:
* * npm start
* Backend:
* * flask run

Installation:
* pip install -r requirements.txt
* npm install web-vitals
* npm install axios

**REMINDER:
* If youre running on ubuntu be sure to use the ubuntu requirements
