# Update package index
sudo apt update

# Install Docker
sudo apt install -y docker.io

# Enable & start Docker service
sudo systemctl enable --now docker

# Verify Docker works
sudo docker run hello-world

docker pull python:3.11


sudo docker rm -f aifast-dev 2>/dev/null && sudo docker run -d -p 8008:8008 -v ~/aifast:/app --name aifast-dev aifast-dev:latest
