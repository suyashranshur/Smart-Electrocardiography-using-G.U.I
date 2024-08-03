import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial

# Define Arduino serial port and baud rate
SERIAL_PORT = 'COM16'  # Change this to your Arduino's serial port
BAUD_RATE = 9600

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)


# Function to read data from serial port
def read_serial_data():
    data = ser.readline().decode().strip()
    try:
        return float(data)
    except ValueError:
        return None


# Function to update the chart
def update_chart(frame):
    global x_data, y_data
    value = read_serial_data()
    if value is not None:
        x_data.append(frame)
        y_data.append(value)
        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
        # Adjust x-axis limits based on frame value and window size
        if frame >= WINDOW_SIZE:
            ax.set_xlim(frame - WINDOW_SIZE, frame)
    return line,


# Create tkinter application
root = tk.Tk()
root.title("ECG Sensor Data")

# Initialize plot variables
x_data, y_data = [], []

# Function to start ECG
def start_ecg():
    global ani, fig, ax, line, WINDOW_SIZE
    # Initialize plot
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    # Set plot properties
    ax.set_xlabel('Time')
    ax.set_ylabel('ECG Value')
    ax.set_title('ECG Sensor Data')

    # Set window size for visible data
    WINDOW_SIZE = 100

    # Create animation
    ani = FuncAnimation(fig, update_chart, blit=True, interval=50, cache_frame_data=False)

    # Embed Matplotlib plot into tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


start_ecg()

# Run tkinter main loop
root.mainloop()

# Close serial connection when tkinter window is closed
ser.close()
