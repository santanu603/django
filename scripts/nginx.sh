
#!/usr/bin/bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/django/nginx/nginx.conf /etc/nginx/sites-available/chq_proj
sudo ln -s /etc/nginx/sites-available/chq_proj /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/chq_proj /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx

