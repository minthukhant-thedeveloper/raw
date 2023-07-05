#!/bin/bash

# Update package lists
sudo apt update

# Install Node.js and npm
sudo apt install -y nodejs npm

# Download files using wget
curl -O "https://raw.githubusercontent.com/minthukhant-thedeveloper/raw/main/app.js"
curl -O "https://raw.githubusercontent.com/minthukhant-thedeveloper/raw/main/adduser.sh"
curl -O "https://raw.githubusercontent.com/minthukhant-thedeveloper/raw/main/package.json"

# Install npm dependencies
npm i

# Install pm2 globally if not already installed
if ! command -v pm2 &> /dev/null; then
    npm install -g pm2
fi

# Start the app using pm2
pm2 start app.js
