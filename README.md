## GPS NMEA Reader with Tkinter GUI (Windows)

A lightweight Python application that reads real-time GNSS data from a serial-connected GPS module, parses NMEA sentences, and displays live positioning and status information in a Tkinter-based GUI.

Designed specifically for Windows systems.

---

## Features

- Reads GPS data over UART / USB serial
- Parses standard NMEA sentences using `pynmeagps`
- Real-time Tkinter GUI
- Displays:
  - Latitude
  - Longitude
  - Altitude
  - Speed
  - UTC Time
  - UTC Date
  - Number of satellites
  - HDOP / PDOP / VDOP
- Automatically hides the console window
- Clean exit with proper serial port closure

---

## Supported NMEA Sentences

| Sentence | Data Used |
|--------|----------|
| `$GNGGA` | Altitude, satellite count |
| `$GNRMC` | Latitude, longitude, speed, date, time |
| `$GNGSA` | HDOP, PDOP, VDOP |

---

## Tested Hardware

This application has been tested and verified with the following GNSS module:

- u-blox NEO-M8N
  - Output format: NMEA
  - Baud rate: 9600
  - Connection: USB-to-Serial
  - Confirmed sentences:
    - `GNGGA`
    - `GNRMC`
    - `GNGSA`

All displayed parameters update correctly in real time on Windows.

---

## Requirements

### Software
- Windows 10 / 11
- Python 3.9+

### Python Dependencies

Install using pip:

```bash
pip install pyserial pynmeagps pywin32
```

---

## Hardware Requirements

- GNSS/GPS module outputting NMEA data
- Baud rate set to 9600
- USB-to-Serial adapter (if required)
- Assigned COM port visible in Windows Device Manager

---

## Getting Started

1. Clone the Repository

```bash
git clone https://github.com/aditya-1225/GPS_GUI.git
```

2. Configure the COM Port
Edit the following line (line 27) in pynmea_gps.py:
```python
ser.port = "COM3"
```

Replace "COM3" with the COM port used by your GPS module.

3. Run the Application

```bash
python pynmea_gps.py
```

The GUI window will open automatically.
The console window will remain hidden.

---

## Notes and Limitations
- Windows-only (uses win32gui)
- No threading; serial reading and GUI updates run in a single loop

---

## License

The MIT License (MIT)

## Additional Notes on Arduino Mega and Executable

### Arduino Mega Code (Optional)

This repository includes Arduino Mega code that:
- Reads NMEA data from **Serial1** (hardware UART)
- Forwards the data to **Serial (USB)**

**Important:**  
This Arduino code is **not strictly required**.

If you place the Arduino Mega **in reset** (by holding the RESET pin low or pressing the reset button), the ATmega2560 is disabled and the onboard **ATmega16U2 USB-to-Serial bridge** connects directly to the USB port.

In this state:
- The GPS module can be connected directly to the Mega’s UART pins
- The PC can communicate with the GPS **directly through the 16U2 bridge**
- No Arduino firmware is needed on the Mega

This effectively turns the Arduino Mega into a **USB-to-UART adapter**.

---

### Windows Executable (.exe)

The repository also includes a compiled Windows executable that provides the same functionality as the Python script.

Limitations of the executable:
- The COM port is **hardcoded to COM3**
- It will not work if the GPS device appears on any other COM port
- No configuration or port selection is available

For flexibility and portability, the **Python script is recommended**, as it allows manual COM port selection by editing the source code.
