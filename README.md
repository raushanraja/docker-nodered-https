### docker-nodered-https


#### Values to change:
- File: `caddy/Caddyfile`
    - yourdomain to your domain
    - CHANGE_TO_YOUR_EMAIL to your email

#### NodeRed Configuration:
- The settings in `settings.js` should be changed to match your setup.
- The default settings.js created after first run only and is located in `nodered_data/settings.js`

#### How to run it
- RUN `docker-compose up` in project folder


#### How to stop it
- RUN `docker-compose down`


#### Caddy config
- File: `caddy/Caddyfile`
    - yourdomain to your domain
    - CHANGE_TO_YOUR_EMAIL to your email
- Make sure there is nothing running on port 80 or 443
- Make sure port 80 is not blocked by your firewall, to avoid problems with Caddy
- All generated files are located in `caddy`

