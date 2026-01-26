#!/bin/bash
#
# This script automates the setup of the Raspberry Radio application.
# It creates a virtual environment, installs dependencies, and sets up
# a systemd service to run the application on boot.
#
# This script must be run with sudo.
#

# --- Configuration ---
# The user that will run the application.
# The project directory should be in this user's home directory.
APP_USER="pi"
# The name of the project directory.
PROJECT_DIR_NAME="raspberry_radio"

# --- Derived paths ---
PROJECT_PATH="/home/${APP_USER}/${PROJECT_DIR_NAME}"
VENV_PATH="${PROJECT_PATH}/venv"

# --- Script ---

# 1. Check for root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (with sudo)."
  exit 1
fi

echo "--- Starting Raspberry Radio setup ---"

# 2. Check if the project directory exists
if [ ! -d "$PROJECT_PATH" ]; then
    echo "Error: Project directory not found at ${PROJECT_PATH}"
    echo "Please make sure the project is cloned/copied to that location."
    exit 1
fi

# 3. Update system and install dependencies
echo "--> Updating package list and installing system dependencies..."
apt-get update
apt-get install -y python3 python3-pip python3-venv

# 4. Create virtual environment
echo "--> Creating Python virtual environment..."
sudo -u ${APP_USER} python3 -m venv "${VENV_PATH}"

# 5. Install Python dependencies
echo "--> Installing Python dependencies from requirements.txt..."
sudo -u ${APP_USER} "${VENV_PATH}/bin/pip" install -r "${PROJECT_PATH}/requirements.txt"

# 6. Create systemd service file
SERVICE_FILE="/etc/systemd/system/raspberry_radio.service"
echo "--> Creating systemd service file at ${SERVICE_FILE}..."

cat > ${SERVICE_FILE} << EOF
[Unit]
Description=Raspberry Radio
After=network.target

[Service]
User=${APP_USER}
Group=${APP_USER}
WorkingDirectory=${PROJECT_PATH}
ExecStart=${VENV_PATH}/bin/python -m raspberry_radio
Restart=always
Type=simple

[Install]
WantedBy=multi-user.target
EOF

# 7. Reload systemd, enable and start the service
echo "--> Reloading systemd and starting the service..."
systemctl daemon-reload
systemctl enable raspberry_radio.service
systemctl start raspberry_radio.service

echo "--- Raspberry Radio setup complete! ---"
echo "The service is now running. You can check its status with:"
echo "sudo systemctl status raspberry_radio.service"
