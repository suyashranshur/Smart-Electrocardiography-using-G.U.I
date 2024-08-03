import time
from customtkinter import *
from PIL import Image
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk, Toplevel
from customtkinter import CTkLabel
import os
import subprocess
from tkinter import ttk, scrolledtext
from tkinter import font, filedialog
import serial
import serial.tools.list_ports
from tkinter import messagebox
import webbrowser
import cv2



app = tk.Tk()

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


window_width = 500  # Window width
window_height = 300  # Window height
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

# Set the window geometry
app.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


def open_image1():

    image5 = Image.open("WhatsApp Image 2024-04-08 at 20.26.14_8f1f5071.jpg")
    resized_image5 = image5.resize((window_width, window_height))
    photo5 = ImageTk.PhotoImage(resized_image5)
    app.title("ECG")
    label5 = tk.Label(app, image=photo5)
    label5.image5 = photo5
    label5.place(x=0, y=0)
    app.after(2200, lambda: app.destroy())

open_image1()
app.mainloop()


app=CTk()
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

app.title("ECG")
#Get the screen width and height
screen_width = 1536#app.winfo_screenwidth()
screen_height =864#app.winfo_screenheight()
print(screen_width)
print(screen_height)

app.geometry(f"{screen_width}x{screen_height - 40}+0+0")  # Adjust -40 based on your taskbar size



img= Image.open("manual.png")
img1=Image.open("gear.png")
img2=Image.open("search.png")
img3=Image.open("picture.png")
img4=Image.open("new-product.png")
img5=Image.open("—Pngtree—medical logo_5157139.png")
img6=Image.open("pngwing.com1.png")
img7=Image.open("icons8-menu-30.png")


#------------------------main window--------------------------------


def home():

    def ecg_monitor():
        def ecg_monitorstart():
            # Path to the software executable
            software_path = r'ECG.exe'
            subprocess.Popen([software_path])

        frame1 = CTkFrame(master=app, fg_color="white", border_color="black", border_width=0.6, corner_radius=7,
                          width=1180,
                          height=700)
        frame1.pack(expand=True)
        frame1.place(relx=0.19, rely=0.0700)
        image6 = Image.open("SinusRhythmLabels.svg.png")
        resized_image6 = image6.resize((700, 600))  # Adjust the size as needed
        photo6 = ImageTk.PhotoImage(resized_image6)
        label6 = tk.Label(app, image=photo6)
        label6.image6 = photo6  # Keep a reference to the photo to prevent garbage collection
        label6.place(x=1390, y=480, anchor="center")  # Adjust x and y coordinates as needed

        image7 = Image.open("maxresdefault.jpg")
        # Resize the image to your desired size
        resized_image7 = image7.resize((600, 400))  # Adjust the size as needed
        # Create a Tkinter-compatible photo image
        photo7 = ImageTk.PhotoImage(resized_image7)
        # Create a label to display the image
        label7 = tk.Label(app, image=photo7)
        label7.image7 = photo7  # Keep a reference to the photo to prevent garbage collection
        # Place the label on the window using place method
        label7.place(x=700, y=580, anchor="center")  # Adjust x and y coordinates as needed

        btnECG = CTkButton(master=app, text="ECG Test", corner_radius=15, fg_color="#FFB6C1", text_color="black",
                           command=lambda: [ecg_test()], hover_color="#0082C6",
                           border_color="black", font=("Constantia", 20),
                           image=CTkImage(dark_image=img2, light_image=img2),
                           border_width=0.4, width=190, height=25)
        btnECG.place(relx=0.265, rely=0.1095, anchor="center")
        btnECGc = CTkButton(master=app, text="ECG Monetering", corner_radius=15, fg_color="#FFB6C1", text_color="black",
                            command=lambda: [ecg_monitor()], hover_color="#0082C6",
                            border_color="black", font=("Constantia", 20),
                            border_width=0.4, width=190, height=25)
        btnECGc.place(relx=0.265, rely=0.16, anchor="center")

        btnstartecg = CTkButton(master=app, text="Start ECG Monitor", corner_radius=15, fg_color="red", text_color="black",
                                command=lambda: [ecg_monitorstart()], hover_color="#0082C6",
                                border_color="black", font=("Constantia", 20),
                                border_width=0.4, width=190, height=25)
        btnstartecg.place(relx=0.565, rely=0.1095, anchor="center")





    def ecg_test():



        def ecg_teststart():
            # Path to the software executable
            software_path = r'ECG_test.exe'
            subprocess.Popen([software_path])


        frame1 = CTkFrame(master=app, fg_color="white", border_color="black", border_width=0.6, corner_radius=7,
                          width=1180,
                          height=700)
        frame1.pack(expand=True)
        frame1.place(relx=0.19, rely=0.0700)
        image6 = Image.open("Limb-lead-placement-pic-with-lables-1024x691.webp")
        # Resize the image to your desired size
        resized_image6 = image6.resize((700, 600))  # Adjust the size as needed
        # Create a Tkinter-compatible photo image
        photo6 = ImageTk.PhotoImage(resized_image6)
        # Create a label to display the image
        label6 = tk.Label(app, image=photo6)
        label6.image6 = photo6  # Keep a reference to the photo to prevent garbage collection
        # Place the label on the window using place method
        label6.place(x=1290, y=480, anchor="center")  # Adjust x and y coordinates as needed

        btnECG = CTkButton(master=app, text="ECG Test", corner_radius=15, fg_color="#FFB6C1", text_color="black",
                           command=lambda: [ecg_test()], hover_color="#0082C6",
                           border_color="black", font=("Constantia", 20),
                           image=CTkImage(dark_image=img2, light_image=img2),
                           border_width=0.4, width=190, height=25)
        btnECG.place(relx=0.265, rely=0.1095, anchor="center")
        btnECGc = CTkButton(master=app, text="ECG Monetering", corner_radius=15, fg_color="#FFB6C1", text_color="black",
                            command=lambda: [ecg_monitor()], hover_color="#0082C6",
                            border_color="black", font=("Constantia", 20),
                            border_width=0.4, width=190, height=25)
        btnECGc.place(relx=0.265, rely=0.16, anchor="center")

        btnstartecg = CTkButton(master=app, text="Start ECG", corner_radius=15, fg_color="red", text_color="black",
                            command=lambda: [ecg_teststart()], hover_color="#0082C6",
                            border_color="black", font=("Constantia", 20),
                            border_width=0.4, width=190, height=25)
        btnstartecg.place(relx=0.565, rely=0.1095, anchor="center")











    frame1 = CTkFrame(master=app, fg_color="white", border_color="black", border_width=0.6, corner_radius=7, width=1180,
                      height=700)
    frame1.pack(expand=True)
    frame1.place(relx=0.19, rely=0.0700)

    image6 = Image.open("main logo.jpg")
    # Resize the image to your desired size
    resized_image6 = image6.resize((600, 400))  # Adjust the size as needed
    # Create a Tkinter-compatible photo image
    photo6 = ImageTk.PhotoImage(resized_image6)
    # Create a label to display the image
    label6 = tk.Label(app, image=photo6)
    label6.image6 = photo6  # Keep a reference to the photo to prevent garbage collection
    # Place the label on the window using place method
    label6.place(x=1313, y=480, anchor="center")  # Adjust x and y coordinates as needed

    frame3 = CTkFrame(master=app, fg_color="#FAFAFA", border_color="black", border_width=0.6, corner_radius=7,
                      width=275, height=458)
    frame3.pack(expand=True)
    frame3.place(relx=0.0094, rely=0.0710)

    btnhome = CTkButton(master=app, text="", corner_radius=13, fg_color="white", width=35, height=20,
                        hover_color="#0082C6",
                        font=("Segoe UI", 13), text_color="black", command=lambda: [home()],
                        border_width=0.2, image=CTkImage(dark_image=img7, light_image=img7))
    btnhome.place(x=250, y=80, anchor="center")
    labelr = tk.Label(app, text=("Reports "), font=("Times New Roman", 15), fg="black", bg="#EBEBEB")
    labelr.place(x=35, y=80, height=40, width=240)
    labelnote = tk.Label(app, text=("Note : This Software is under\nTraining Mode"), font=("Times New Roman", 18),
                         fg="black", bg="white")
    labelnote.place(x=1460, y=800, height=100, width=300)

    def nearbyhospital():
        frame4 = CTkFrame(master=app, fg_color="#FAFAFA", border_color="black", border_width=0.6, corner_radius=7,
                          width=275, height=237)
        frame4.pack(expand=True)
        frame4.place(relx=0.0094, rely=0.6310)
        btnhospital = CTkButton(master=app, text="Nearby Hospitals", corner_radius=7, fg_color="#EBEBEB",
                                text_color="black",
                                command=lambda: [leftscreen()], hover_color="#0082C6",
                                border_color="black", font=("Segoe UI", 13),
                                image=CTkImage(dark_image=img2, light_image=img2),
                                border_width=0, width=230, height=20)
        btnhospital.place(x=150, y=550, anchor="center")

        # ------------main logic------------------------
        btnpune = CTkButton(master=app, text="Pune", corner_radius=7, fg_color="#FAFAD2",
                            text_color="black",
                            command=lambda: os.startfile("https://www.google.com/maps/search/hospitals+in+Pune"),
                            hover_color="#0082C6",
                            border_color="black", font=("Segoe UI", 13), width=200, height=15)
        btnpune.place(x=150, y=580, anchor="center")
        btnmumbai = CTkButton(master=app, text="Mumbai", corner_radius=7, fg_color="#FAFAD2",
                              text_color="black",
                              command=lambda: os.startfile("https://www.google.com/maps/search/hospitals+in+Mumbai"),
                              hover_color="#0082C6",
                              border_color="black", font=("Segoe UI", 13), width=200, height=15)
        btnmumbai.place(x=150, y=605, anchor="center")
        btnnagpur = CTkButton(master=app, text="Nagpur", corner_radius=7, fg_color="#FAFAD2",
                              text_color="black",
                              command=lambda: os.startfile("https://www.google.com/maps/search/hospitals+in+Nagpur"),
                              hover_color="#0082C6",
                              border_color="black", font=("Segoe UI", 13), width=200, height=15)
        btnnagpur.place(x=150, y=630, anchor="center")

        btnecginst = CTkButton(master=app, text="ECG Instruction", corner_radius=7, fg_color="#EBEBEB",
                               text_color="black",
                               command=lambda: os.startfile("Final_PATIENT-INSTRUCTIONS-ECG-Holter-and-Stress.pdf"),
                               hover_color="#0082C6",
                               image=CTkImage(dark_image=img, light_image=img),
                               border_color="black", font=("Segoe UI", 14),
                               border_width=0, width=230, height=20)
        btnecginst.place(x=150, y=670, anchor="center")
        btnmed = CTkButton(master=app, text="Medicine", corner_radius=7, fg_color="#EBEBEB", text_color="black",
                           command=lambda: [server_click()], hover_color="#0082C6",
                           image=CTkImage(dark_image=img5, light_image=img5),
                           border_color="black", font=("Segoe UI", 14),
                           border_width=0, width=230, height=20)
        btnmed.place(x=150, y=700, anchor="center")
        btnmed = CTkButton(master=app, text=" Attack First AID", corner_radius=7, fg_color="#EBEBEB",
                           text_color="black",
                           command=lambda: [heartattachfirstaid()], hover_color="#0082C6",
                           image=CTkImage(dark_image=img6, light_image=img6),
                           border_color="black", font=("Segoe UI", 14),
                           border_width=0, width=230, height=20)
        btnmed.place(x=150, y=730, anchor="center")

    def heartattachfirstaid():

        def warning():
            frame1 = CTkFrame(master=app, fg_color="white", border_color="black", border_width=0.6, corner_radius=7,
                              width=1180,
                              height=700)
            frame1.pack(expand=True)
            frame1.place(relx=0.19, rely=0.0700)
            image6 = Image.open("warning-signs-of-heart-attack-1-1024x723.jpg")
            # Resize the image to your desired size
            resized_image6 = image6.resize((700, 800))  # Adjust the size as needed
            # Create a Tkinter-compatible photo image
            photo6 = ImageTk.PhotoImage(resized_image6)
            # Create a label to display the image
            label6 = tk.Label(app, image=photo6)
            label6.image6 = photo6  # Keep a reference to the photo to prevent garbage collection
            # Place the label on the window using place method
            label6.place(x=1290, y=480, anchor="center")  # Adjust x and y coordinates as needed

            btncpr = CTkButton(master=app, text="CPR Instruction", corner_radius=7, fg_color="#BFEFFF",
                               text_color="black",
                               command=lambda: [cpr()], hover_color="#0082C6",

                               border_color="black", font=("Segoe UI", 14),
                               border_width=0.8, width=230, height=25)
            btncpr.place(x=430, y=150, anchor="center")
            btnwarnin = CTkButton(master=app, text="Warning Signs", corner_radius=7, fg_color="#BFEFFF",
                                  text_color="black",
                                  command=lambda: [warning()], hover_color="#0082C6",

                                  border_color="black", font=("Segoe UI", 14),
                                  border_width=0.8, width=230, height=25)
            btnwarnin.place(x=430, y=190, anchor="center")

            labelnote = tk.Label(app, text=("Watch Video how to \n do CPR."), font=("Times New Roman", 18),
                                 fg="black", bg="white")
            labelnote.place(x=380, y=280, height=100, width=300)

            btncprvid = CTkButton(master=app, text="Watch Video", corner_radius=7, fg_color="#BFEFFF",
                                  text_color="black",
                                  command=lambda: [os.startfile("https://www.youtube.com/watch?v=G87knTZnhks")],
                                  hover_color="#0082C6",

                                  border_color="black", font=("Segoe UI", 14),
                                  border_width=0.8, width=230, height=25)
            btncprvid.place(x=430, y=310, anchor="center")

        def cpr():
            frame1 = CTkFrame(master=app, fg_color="white", border_color="black", border_width=0.6, corner_radius=7,
                              width=1180,
                              height=700)
            frame1.pack(expand=True)
            frame1.place(relx=0.19, rely=0.0700)
            image6 = Image.open("7661-cpr-hand-position-1296x728-body-1296x1979.webp")
            # Resize the image to your desired size
            resized_image6 = image6.resize((700, 800))  # Adjust the size as needed
            # Create a Tkinter-compatible photo image
            photo6 = ImageTk.PhotoImage(resized_image6)
            # Create a label to display the image
            label6 = tk.Label(app, image=photo6)
            label6.image6 = photo6  # Keep a reference to the photo to prevent garbage collection
            # Place the label on the window using place method
            label6.place(x=1290, y=480, anchor="center")  # Adjust x and y coordinates as needed

            btncpr = CTkButton(master=app, text="CPR Instruction", corner_radius=7, fg_color="#BFEFFF",
                               text_color="black",
                               command=lambda: [cpr()], hover_color="#0082C6",

                               border_color="black", font=("Segoe UI", 14),
                               border_width=0.8, width=230, height=25)
            btncpr.place(x=430, y=150, anchor="center")
            btnwarnin = CTkButton(master=app, text="Warning Signs", corner_radius=7, fg_color="#BFEFFF",
                                  text_color="black",
                                  command=lambda: [warning()], hover_color="#0082C6",

                                  border_color="black", font=("Segoe UI", 14),
                                  border_width=0.8, width=230, height=25)
            btnwarnin.place(x=430, y=190, anchor="center")

            labelnote = tk.Label(app, text=("Watch Video how to \n do CPR."), font=("Times New Roman", 18),
                                 fg="black", bg="white")
            labelnote.place(x=380, y=280, height=100, width=300)

            btncprvid = CTkButton(master=app, text="Watch Video", corner_radius=7, fg_color="#BFEFFF",
                                  text_color="black",
                                  command=lambda: [os.startfile("https://www.youtube.com/watch?v=G87knTZnhks")],
                                  hover_color="#0082C6",

                                  border_color="black", font=("Segoe UI", 14),
                                  border_width=0.8, width=230, height=25)
            btncprvid.place(x=430, y=310, anchor="center")

        frame1 = CTkFrame(master=app, fg_color="white", border_color="black", border_width=0.6, corner_radius=7,
                          width=1180,
                          height=700)
        frame1.pack(expand=True)
        frame1.place(relx=0.19, rely=0.0700)

        image6 = Image.open("First-Aid-during-heart-attack-CPR-Guide-step-by-step-1024x576.jpg")
        # Resize the image to your desired size
        resized_image6 = image6.resize((1050, 600))  # Adjust the size as needed
        # Create a Tkinter-compatible photo image
        photo6 = ImageTk.PhotoImage(resized_image6)
        # Create a label to display the image
        label6 = tk.Label(app, image=photo6)
        label6.image6 = photo6  # Keep a reference to the photo to prevent garbage collection
        # Place the label on the window using place method
        label6.place(x=1290, y=480, anchor="center")  # Adjust x and y coordinates as needed

        btncpr = CTkButton(master=app, text="CPR Instruction", corner_radius=7, fg_color="#BFEFFF", text_color="black",
                           command=lambda: [cpr()], hover_color="#0082C6",

                           border_color="black", font=("Segoe UI", 14),
                           border_width=0.8, width=230, height=25)
        btncpr.place(x=430, y=150, anchor="center")
        btnwarnin = CTkButton(master=app, text="Warning Signs", corner_radius=7, fg_color="#BFEFFF", text_color="black",
                              command=lambda: [warning()], hover_color="#0082C6",

                              border_color="black", font=("Segoe UI", 14),
                              border_width=0.8, width=230, height=25)
        btnwarnin.place(x=430, y=190, anchor="center")

    # ----------------------left corner screen-----------------------------------
    def leftscreen():
        frame4 = CTkFrame(master=app, fg_color="#FAFAFA", border_color="black", border_width=0.6, corner_radius=7,
                          width=275, height=237)
        frame4.pack(expand=True)
        frame4.place(relx=0.0094, rely=0.6310)
        btnhospital = CTkButton(master=app, text="Nearby Hospitals", corner_radius=7, fg_color="#EBEBEB",
                                text_color="black",
                                command=lambda: [nearbyhospital()], hover_color="#0082C6",
                                border_color="black", font=("Segoe UI", 14),
                                image=CTkImage(dark_image=img2, light_image=img2),
                                border_width=0, width=230, height=25)
        btnhospital.place(x=150, y=550, anchor="center")
        btnecginst = CTkButton(master=app, text="ECG Instruction", corner_radius=7, fg_color="#EBEBEB",
                               text_color="black",
                               command=lambda: os.startfile("Final_PATIENT-INSTRUCTIONS-ECG-Holter-and-Stress.pdf"),
                               hover_color="#0082C6",
                               image=CTkImage(dark_image=img, light_image=img),
                               border_color="black", font=("Segoe UI", 14),
                               border_width=0, width=230, height=25)
        btnecginst.place(x=150, y=585, anchor="center")
        btnmed = CTkButton(master=app, text="Medicine", corner_radius=7, fg_color="#EBEBEB", text_color="black",
                           command=lambda: [server_click()], hover_color="#0082C6",
                           image=CTkImage(dark_image=img5, light_image=img5),
                           border_color="black", font=("Segoe UI", 14),
                           border_width=0, width=230, height=25)
        btnmed.place(x=150, y=620, anchor="center")
        btnmedaid = CTkButton(master=app, text=" Attack First AID", corner_radius=7, fg_color="#EBEBEB",
                              text_color="black",
                              command=lambda: [heartattachfirstaid()], hover_color="#0082C6",
                              image=CTkImage(dark_image=img6, light_image=img6),
                              border_color="black", font=("Segoe UI", 14),
                              border_width=0, width=230, height=25)
        btnmedaid.place(x=150, y=655, anchor="center")


        def sos():
            os.startfile("https://pune.gov.in/public-utility/aundh-government-hospital/")
        btnsos = CTkButton(master=app, text="Emergency Contact", corner_radius=7, fg_color="red", text_color="black",
                           command=lambda: [sos()], hover_color="#0082C6",

                           border_color="black", font=("Segoe UI", 14),
                           border_width=0, width=230, height=25)
        btnsos.place(x=150, y=690, anchor="center")

    leftscreen()

    btnECG = CTkButton(master=app, text="ECG Test", corner_radius=15, fg_color="#FFB6C1", text_color="black",
                       command=lambda: [ecg_test()], hover_color="#0082C6",
                       border_color="black", font=("Constantia", 20), image=CTkImage(dark_image=img2, light_image=img2),
                       border_width=0.4, width=190, height=25)
    btnECG.place(relx=0.265, rely=0.1095, anchor="center")
    btnECGc = CTkButton(master=app, text="ECG Monetering", corner_radius=15, fg_color="#FFB6C1", text_color="black",
                        command=lambda: [ecg_monitor()], hover_color="#0082C6",
                        border_color="black", font=("Constantia", 20),
                        border_width=0.4, width=190, height=25)
    btnECGc.place(relx=0.265, rely=0.16, anchor="center")

    btnhelp = CTkButton(master=app, text="About", corner_radius=13, fg_color="white", width=27, height=20,
                        hover_color="#0082C6",
                        font=("Segoe UI", 13), text_color="black", command=lambda: [about()],
                        border_width=0.2, image=CTkImage(dark_image=img2, light_image=img2))
    btnhelp.place(relx=0.92, rely=0.047, anchor="center")
    btnreport = CTkButton(master=app, text="Project Report", corner_radius=13, fg_color="white", width=35, height=20,
                          hover_color="#0082C6",
                          font=("Segoe UI", 13), text_color="black", command=lambda: [Report()],
                          border_width=0.2, image=CTkImage(dark_image=img3, light_image=img3))
    btnreport.place(relx=0.84, rely=0.047, anchor="center")
    btnppt = CTkButton(master=app, text="Project  PPT", corner_radius=13, fg_color="white", width=35, height=20,
                       hover_color="#0082C6",
                       font=("Segoe UI", 13), text_color="black", command=lambda: [PPT()],
                       border_width=0.2, image=CTkImage(dark_image=img4, light_image=img4))
    btnppt.place(relx=0.747, rely=0.047, anchor="center")

    def Report():
        os.startfile("Electrocardiography Report.pdf")

    def PPT():
        os.startfile("PPT_TE.pptx")

    def about():
        # Function to handle what happens when the About button is clicked
        top = CTkToplevel()  # Create a new window
        top.title("About")  # Set the title of the window

        # Add content to the popup screen
        labelab = CTkLabel(top, text="Softwere Ver. 0.1\nUpdated . 15/04/2024\nDeveloped By :Suyash Ranshur",
                           width=250, height=100)
        labelab.pack()

        # You can add more widgets and customize the content of the popup screen here
        top.grab_set()

        # Set the position of the popup window relative to the root window
        window_width = top.winfo_reqwidth()
        window_height = top.winfo_reqheight()
        screen_width = top.winfo_screenwidth()
        screen_height = top.winfo_screenheight()
        x = int((screen_width - window_width) * 0.5)
        y = int((screen_height - window_height) * 0.5)
        top.geometry(f"+{x}+{y}")

    def reportsshow():
        # Specify the folder path
        folder_path = "D:/photoshop"

        def open_file(file_path):
            # Open the file using the default application
            subprocess.Popen([file_path], shell=True)

        def create_buttons():
            # Clear previous buttons
            for button in buttons:
                button.destroy()
            buttons.clear()

            max_filename_length = max(
                len(file_name) for file_name in os.listdir(folder_path) if file_name.endswith('.xlsx'))
            y_position = 140
            button_height = 33  # Adjust the button height as needed
            vertical_spacing = 8  # Adjust the vertical spacing between buttons
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.xlsx'):  # Filter only Excel files
                    file_path = os.path.join(folder_path, file_name)
                    button = tk.Button(app, text=file_name, command=lambda path=file_path: open_file(path),
                                       width=33, font=("Segoe UI Emoji", 12))  # Set the font and width
                    if len(buttons) % 2 == 0:
                        button.config(bg='#FAFAD2', fg='black')  # Alternate button colors
                    else:
                        button.config(bg='#FAFAD2')
                    button.place(x=35, y=y_position)
                    y_position += button_height + vertical_spacing  # Increase y position with spacing
                    buttons.append(button)

            # Schedule the create_buttons function to run again after 10 seconds
            app.after(10000, create_buttons)

        # Create a custom font
        custom_font = font.Font(family="Arial", size=10)  # Change family and size as needed
        # Create a list to store buttons
        buttons = []
        # Display the files as buttons
        create_buttons()

    reportsshow()
home()
app.mainloop()


