import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import serial
import os
from openpyxl import load_workbook
from openpyxl.chart import LineChart, Reference

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


# Function to update the chart and save data to Excel after 300 readings
def update_chart(frame):
    global x_data, y_data, readings
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
        readings.append(value)
        if len(readings) == 500:
            print("Saving data to Excel...")
            save_to_excel()
    return line,


# Function to save data to Excel and open the file
def save_to_excel():
    data = {'Readings': x_data, 'Mili_VTG': y_data}
    df = pd.DataFrame(data)
    try:
        # Specify the file path to save
        filename = r'D:\photoshop\ecg_data.xlsx'
        df.to_excel(filename, index=False)
        print(f"Data saved to '{filename}'")
        # Open the Excel file using the default application
        os.startfile(filename)

        # Add 2D line graph to the Excel sheet
        add_line_chart(filename, df)
    except Exception as e:
        print(f"Error saving data to Excel: {e}")
    plt.close()


# Function to add 2D line chart to Excel sheet
# Function to add 2D line chart to Excel sheet with Chart design Style 10
def add_line_chart(filename, df):
    wb = load_workbook(filename)
    ws = wb.active

    chart = LineChart()
    chart.title = "MiliVTG Readings"
    chart.y_axis.title = "Mili_VTG"
    chart.x_axis.title = "Readings"
    data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=len(df['Mili_VTG']))
    categories = Reference(ws, min_col=1, min_row=2, max_row=len(df['Mili_VTG']))
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)
    chart.style = 1  # Set the style to Chart design Style 10
    ws.add_chart(chart, "D5")

    wb.save(filename)



# Create tkinter application
root = tk.Tk()
root.title("ECG Sensor Data")

# Initialize plot variables
x_data, y_data = [], []
readings = []


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
