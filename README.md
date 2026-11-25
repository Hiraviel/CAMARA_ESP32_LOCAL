# CAMARA_ESP32_LOCAL

Small Python script that grabs a photo from an ESP32-CAM over the local network every minute and saves it to disk.

## What it does

- Polls the camera once every 60 seconds, in an infinite loop.
- Downloads the current frame from the camera and saves it as a timestamped `.jpg` file in the script's folder (for example `2022-08-29_02_47_00.jpg`).
- Rotates each captured image −90° before saving it, so the photos come out with the correct orientation.

## Requirements

- Python 3
- `requests` (HTTP download from the camera)
- `Pillow` (image rotation)
- An ESP32-CAM on the same local Wi-Fi network, serving a photo endpoint

## Setup

1. Install the dependencies:

   ```bash
   pip install requests Pillow
   ```

2. Set the camera's local IP address in `accesar_esp32.py` (the script reaches the camera over HTTP on your LAN).

3. Run it:

   ```bash
   python accesar_esp32.py
   ```

   Photos are saved in the current folder, one per minute, until you stop the script with `Ctrl+C`.

## File layout

| File | Description |
| --- | --- |
| `accesar_esp32.py` | The whole project: capture loop, download, rotation, and saving |

## Notes

- The script has no configuration file — the camera address and the 60-second interval are set directly in the code.
- Filenames use the local date and time of each capture, so photos never overwrite each other.
