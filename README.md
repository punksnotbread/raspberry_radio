# raspberry_radio
Change through internet radios by using a button connected to the RPI via GPIO.

Based on https://pinout.xyz/ , an example setup would be ground on 6, GPIO 14 on 8th pin.

## TODOs
- Move logging to separate class.
- Add other radios.
- Make this configureable via config.
- Daemonize.

### Daemonize (linux)
```
[Unit]
Description=Raspberry Radio
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/<PATH_TO_VENV>/python3 /<PATH_TO_REPO>/raspberry_radio/main.py

[Install]
WantedBy=multi-user.target
```

```
sudo vim /etc/systemd/system/raspberry_radio.service
sudo systemctl daemon-reload
sudo systemctl enable raspberry_radio.service
sudo systemctl start raspberry_radio
sudo systemctl status raspberry_radio
```