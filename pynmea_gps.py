import serial
import serial.tools.list_ports
import win32gui, win32con
import tkinter as tk
import os
from pynmeagps import NMEAReader

# Initialize serial port
ser = serial.Serial()
ser.baudrate = 9600  # Set baud rate to 9600
ser.bytesize = serial.EIGHTBITS  # 8 data bits
ser.parity = serial.PARITY_NONE  # No parity bit
ser.stopbits = serial.STOPBITS_ONE  # 1 stop bit

# Get available serial ports
ports = serial.tools.list_ports.comports() 

# Hide the console window
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

# Print available ports
for port in ports:
    print(port)

# Set the desired port (modify as needed)
ser.port = "COM3"  # Change to the appropriate port
ser.open()  # Open serial port

# Check if the port is open
if ser.isOpen():
    print("Port is open")
else:
    print("Port is not open")


# Functions to parse GPS data
# Returns the current latitude reading
def get_latitude(msg):
    if msg.lat == "" or msg.lat is None:
        return "Latitude error"
    else:
        latitude1 = round(float(msg.lat), 7)
        return f"{latitude1}°N"

# Returns the current longitude reading
def get_longitude(msg):
    if msg.lon == "" or msg.lon is None:
        return "Longitude error"
    else:
        longitude1 = round(float(msg.lon), 7)
        return f"{longitude1}°E"

# Returns the current altitude reading
def get_altitude(msg):
    if msg.alt == "" or msg.alt is None:
        return "Altitude error"
    else:
        altitude = round(float(msg.alt) / 1, 3)
        return f"{altitude} m"

# Returns the number of satellites currently visible to the receiver
def get_sat_num(msg):
    num_of_sat = msg.numSV
    return f"{num_of_sat}"

# Returns the current speed of the receiver
def get_spd(msg):
    if msg.spd == "" or msg.spd is None:
        return "Speed error"
    else:
        speed_m_per_s = msg.spd
        speed = round(float(speed_m_per_s), 7)
        return f"{speed} m/s"

# Returns the current UTC time 
def get_time(msg):
    time = msg.time
    return f"{time}"

# Returns the current UTC date
def get_date(msg):
    date = msg.date
    return f"{date}"

# Returns position dilution of precision
def get_pdop(msg):
    pdop = msg.PDOP
    return f"{pdop}"

# Returns horizontal dilution of precision
def get_hdop(msg):
    hdop = msg.HDOP
    return f"{hdop}"

# Returns vertical dilution of precision
def get_vdop(msg):
    vdop = msg.VDOP
    return f"{vdop}"


gsa = True  # Flag to process GNGSA message

# Create GUI using Tkinter
root = tk.Tk()
root.title("GNS data")  # Window title
root.configure(bg="black")  # Set background color

# Create StringVar variables to store real-time GPS data
latitude_var = tk.StringVar()
longitude_var = tk.StringVar()
altitude_var = tk.StringVar()
sat_num_var = tk.StringVar()
spd_var = tk.StringVar()
time_var = tk.StringVar()
date_var = tk.StringVar()
hdop_var = tk.StringVar()
pdop_var = tk.StringVar()
vdop_var = tk.StringVar()

# Create Label widgets for the labels and values
tk.Label(root, text="Latitude: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=0, column=0, sticky="w"
)
tk.Label(
    root, textvariable=latitude_var, bg="black", fg="white", font=("Arial", 20)
).grid(row=0, column=1, sticky="w")

tk.Label(root, text="Longitude: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=1, column=0, sticky="w"
)
tk.Label(
    root, textvariable=longitude_var, bg="black", fg="white", font=("Arial", 20)
).grid(row=1, column=1, sticky="w")

tk.Label(root, text="Altitude: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=2, column=0, sticky="w"
)
tk.Label(
    root, textvariable=altitude_var, bg="black", fg="white", font=("Arial", 20)
).grid(row=2, column=1, sticky="w")

tk.Label(
    root, text="No. of satellites: ", bg="black", fg="white", font=("Arial", 20)
).grid(row=3, column=0, sticky="w")
tk.Label(
    root, textvariable=sat_num_var, bg="black", fg="white", font=("Arial", 20)
).grid(row=3, column=1, sticky="w")

tk.Label(root, text="Speed: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=4, column=0, sticky="w"
)
tk.Label(root, textvariable=spd_var, bg="black", fg="white", font=("Arial", 20)).grid(
    row=4, column=1, sticky="w"
)

tk.Label(root, text="Time: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=5, column=0, sticky="w"
)
tk.Label(root, textvariable=time_var, bg="black", fg="white", font=("Arial", 20)).grid(
    row=5, column=1, sticky="w"
)

tk.Label(root, text="Date: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=6, column=0, sticky="w"
)
tk.Label(root, textvariable=date_var, bg="black", fg="white", font=("Arial", 20)).grid(
    row=6, column=1, sticky="w"
)

tk.Label(root, text="HDOP: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=7, column=0, sticky="w"
)
tk.Label(root, textvariable=hdop_var, bg="black", fg="white", font=("Arial", 20)).grid(
    row=7, column=1, sticky="w"
)

tk.Label(root, text="PDOP: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=8, column=0, sticky="w"
)
tk.Label(root, textvariable=pdop_var, bg="black", fg="white", font=("Arial", 20)).grid(
    row=8, column=1, sticky="w"
)

tk.Label(root, text="VDOP: ", bg="black", fg="white", font=("Arial", 20)).grid(
    row=9, column=0, sticky="w"
)
tk.Label(root, textvariable=vdop_var, bg="black", fg="white", font=("Arial", 20)).grid(
    row=9, column=1, sticky="w"
)

# Function to exit the application
def exit1():
    ser.close()  # Close the serial port connection
    root.destroy()  # Close the Tkinter GUI window
    os._exit(0)  # Forcefully terminate the program

# Create exit button
button = tk.Button(
    root,
    text="Exit",
    bg="white",
    fg="black",
    bd=1,
    font=("Arial", 20),
    activebackground="white",
    command=exit1,
)
button.grid(row=0, column=2, sticky="w")

# Read and update GPS data in real-time
while True:
    data = ser.readline().decode("ascii", errors="replace")  # Read and decode serial data

    if data.startswith("$GNGGA"):  # Parse GGA message
        msg = NMEAReader.parse(data)
        altitude_var.set(get_altitude(msg))
        sat_num_var.set(get_sat_num(msg))

    if data.startswith("$GNRMC"):  # Parse RMC message
        msg = NMEAReader.parse(data)
        latitude_var.set(get_latitude(msg))
        longitude_var.set(get_longitude(msg))
        spd_var.set(get_spd(msg))
        time_var.set(get_time(msg))
        date_var.set(get_date(msg))
        gsa = True  # Enable GSA message processing

    if data.startswith("$GNGSA") and gsa == True:  # Parse RMC message
        msg = NMEAReader.parse(data)
        pdop_var.set(get_pdop(msg))
        hdop_var.set(get_hdop(msg))
        vdop_var.set(get_vdop(msg))
        gsa = False  # Disable GSA processing until next cycle

    root.update_idletasks()
    root.update()  # Update GUI with new data
