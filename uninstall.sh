#!/bin/bash
#
# This script uninstalls the Raspberry Radio application.
# It stops and disables the systemd service and removes the service file.
#
# This script must be run with sudo.
#

# --- Script ---

# 1. Check for root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (with sudo)."
  exit 1
fi

echo "--- Starting Raspberry Radio uninstallation ---"

SERVICE_FILE="/etc/systemd/system/raspberry_radio.service"

# 2. Check if the service file exists
if [ ! -f "$SERVICE_FILE" ]; then
    echo "Service file not found at ${SERVICE_FILE}. Nothing to do."
    exit 0
fi

# 3. Stop and disable the service
echo "--> Stopping and disabling the systemd service..."
systemctl stop raspberry_radio.service
systemctl disable raspberry_radio.service

# 4. Remove the systemd service file
echo "--> Removing the systemd service file..."
rm ${SERVICE_FILE}

# 5. Reload systemd
echo "--> Reloading systemd..."
systemctl daemon-reload

echo "--- Raspberry Radio uninstallation complete! ---"
echo "The systemd service has been removed."
echo "The application code and virtual environment have not been deleted."
