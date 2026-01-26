# raspberry_radio
Change through internet radios by using a button connected to the RPI via GPIO, or via local webserver. 

Radio stations are defined in `library.py`.

### Requirements

This project is intended to be used with **Python 3.10.9**.

### Quick Installation (Raspberry Pi)

This project includes scripts to automate the setup on a Raspberry Pi.

1.  **Copy the project to your Pi:**
    Make sure the entire project directory is on your Raspberry Pi, for example at `/home/pi/raspberry_radio`.

    You can use `rsync` to do this. Here is an example command to run on your local machine:
    ```bash
    rsync -avz --exclude '.git' --exclude 'venv' . pi@raspberrypi.local:/home/pi/raspberry_radio/
    ```

2.  **Make scripts executable:**
    ```bash
    chmod +x setup.sh
    chmod +x uninstall.sh
    ```

3.  **Run the setup script:**
    This will install system dependencies, create a virtual environment, install Python packages, and set up a systemd service to run the radio on boot.
    ```bash
    sudo ./setup.sh
    ```
    The application will start automatically. You can check its status with:
    ```bash
    sudo systemctl status raspberry_radio.service
    ```

### Uninstallation

To remove the systemd service and stop the application, run the uninstall script:
```bash
sudo ./uninstall.sh
```

### Manual Setup

If you prefer to set up the project manually:

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

2.  **Activate it and install dependencies:**
    ```bash
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python -m raspberry_radio
    ```

## TODOs
- [x] Move logging to separate class (and log better).
- [x] Add other radio stations.
- [ ] Make this configurable via config.
- [x] Daemonize.
- [ ] Test.
- [ ] Lint.
- [ ] Typehint.
- [x] Make it possible to switch through the stations via HTTP requests? (e.g. build a listener server?)
- [ ] Save library to json.
- [ ] Load library from json.
- [ ] Support add/removal of sources via webserver.
- [ ] Fix requirements (it still requires to reinstall `RPi.GPIO` on some occasions?)
- [ ] Metrics? (e.g. how much time is spent being on one or the other station)
