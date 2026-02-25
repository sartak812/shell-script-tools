#!/bin/bash

# Run this script using: sudo ./rescue.sh

#Step 1: The Setup (apt)
apt update
apt install nginx -y

# Step 2: The Loop (for, chmod, chown)
for ((i=1; i<=3; i++)); do
    touch "/var/www/html/page$i.html"
    chmod 644 /var/www/html/page$i.html
    chown www-data:www-data "/var/www/html/page$i.html"
done

# Step 3: The Logic (if/else, systemctl)
if systemctl is-active --quiet nginx; then
    echo "Nginx is running. Restarting nginx ..."
    systemctl restart nginx
else
    echo "Nginx is dead. Starting nginx..."
    systemctl start nginx
fi

# Step 4: The Proof (journalctl)
journalctl -u nginx -n 5