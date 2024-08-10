### docker-nodered-https


#### Images:
- portainer/portainer-ce:latest
- caddy:latest
- nodered/node-red:latest
- emqx:latest

#### Values to change:
- File: `caddy/Caddyfile`
    - yourdomain to your domain
    - CHANGE_TO_YOUR_EMAIL to your email

#### NodeRed Configuration:
- The settings in `settings.js` should be changed to match your setup.
- The default settings.js created after first run only and is located in `nodered_data/settings.js`

#### EMQX Configuration:
- Add required cert files in emqx/certs directory

#### How to run it
- RUN `docker-compose up` in project folder


#### How to stop it
- RUN `docker-compose down`


#### Things to check after first run
- Please update/set the portainer password on the webpage: https://portainer.yourdomain.com
    - Change the domain to your domain
- Please update settingsj.js to add password to NodeRed

#### Caddy config
- File: `caddy/Caddyfile`
    - yourdomain to your domain
    - CHANGE_TO_YOUR_EMAIL to your email
- Add required certs for EMQX
- Make sure there is nothing running on port 80 or 443
- Make sure port 80 is not blocked by your firewall, to avoid problems with Caddy
- All generated files are located in `caddy`

