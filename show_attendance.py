import csv
import os
import subprocess
import sys
import tkinter
from glob import glob
from tkinter import *
from tkinter import ttk

import pandas as pd

darksem = "#252526"


def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject == "":
            t = 'Please enter the subject name.'
            text_to_speech(t)
        os.chdir(
            f"/home/manjaro/Downloads/face_reco/Attendance/{Subject}"
        )
        filenames = glob(
            f"/home/manjaro/Downloads/face_reco/Attendance/{Subject}/{Subject}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100))) + '%'
            # newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv("attendance.csv", index=False)

        root = tkinter.Tk()
        root.title("Attendance of " + Subject)
        root.configure(background="black")
        cs = f"/home/manjaro/Downloads/face_reco/Attendance/attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:
                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    subject = Tk()
    # tell tcl where to find the awthemes packages
    subject.tk.eval("""
    set base_theme_dir /home/manjaro/Downloads/face_reco/Themes/awthemes

    package ifneeded awthemes 10.4.0 \
        [list source [file join $base_theme_dir awthemes.tcl]]
    package ifneeded colorutils 4.8 \
        [list source [file join $base_theme_dir colorutils.tcl]]
    package ifneeded awdark 7.12 \
        [list source [file join $base_theme_dir awdark.tcl]]
    package ifneeded awlight 7.6 \
        [list source [file join $base_theme_dir awlight.tcl]]
    """)
    # load the awdark and awlight themes
    subject.tk.call("package", "require", 'awdark')
    subject.tk.call("package", "require", 'awlight')

    s = ttk.Style(subject)
    s.theme_use('awdark')

    subject.title("Show Attendance")
    subject.geometry("500x200")
    subject.resizable(0, 0)
    subject.configure(background=darksem)
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    # l1 = ttk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = ttk.Label(
        subject,
        text="Which Subject of Attendance?",
        font=("arial", 25),
    )
    titl.place(relx=0.5, rely=0.1, anchor=CENTER)

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            f = f"/home/manjaro/Downloads/face_reco/Attendance/{sub}"
            subprocess.call([opener, f])

    attf = ttk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        width=18,
    )
    attf.place(relx=0.63, rely=0.7, anchor=CENTER)

    sub = ttk.Label(
        subject,
        text="Enter Subject:",
        width=18,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(relx=0.1, rely=0.4, anchor=W)

    tx = ttk.Entry(
        subject,
        width=30,
        font=("times", 30, "bold"),
    )
    tx.place(relx=0.4, rely=0.4, anchor=W)

    viewBTN = ttk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        width=18,
    )
    viewBTN.place(relx=0.33, rely=0.7, anchor=CENTER)
    subject.mainloop()
