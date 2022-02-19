# raspberry_radio
Change through internet radios by using a button connected to the RPI via GPIO, or via local webserver. 

Radio stations are defined in `library.py`.

### Setup
Based on https://pinout.xyz/ , an example setup would be ground on 6, GPIO 14 on 8th pin.
```
python3 -m venv venv
source venv/bin/activate
python -r requirements.txt
```

### Local testing
```
venv/bin/python main.py
```

## TODOs
- [x] Move logging to separate class (and log better).
- [x] Add other radio stations.
- [ ] Make this configurable via config.
- [ ] Daemonize.
- [ ] Test.
- [ ] Lint.
- [ ] Typehint.
- [x] Make it possible to switch through the stations via HTTP requests? (e.g. build a listener server?)
- [ ] Save library to json.
- [ ] Load library from json.
- [ ] Support add/removal of sources via webserver.
- [ ] Fix requirements (it still requires to reinstall `RPi.GPIO` on some occasions?)
- [ ] Metrics? (e.g. how much time is spent being on one or the other station)

### Daemonize (linux)
```
[Unit]
Description=Raspberry Radio
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/<PATH_TO_VENV>/python3 /<PATH_TO_REPO>/raspberry_radio/src/main.py

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
