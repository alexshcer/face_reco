import cv2
import datetime
import os
import subprocess
import sys
import time
from tkinter import *
from tkinter import ttk

import pandas as pd

haarcasecade_path = "/home/manjaro/Downloads/face_reco/haarcascade_frontalface_default.xml"
trainimagelabel_path = "/home/manjaro/Downloads/face_reco/TrainingImageLabel/Trainner.yml"
trainimage_path = "/home/manjaro/Downloads/face_reco/TrainingImage"
studentdetail_path = "/home/manjaro/Downloads/face_reco/StudentDetails/studentdetails.csv"
attendance_path = "/home/manjaro/Downloads/face_reco/Attendance"

darksem = "#252526"


# for choose subject and fill attendance
def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()
        now = time.time()
        future = now + 20
        print(now)
        print(future)
        if sub == "":
            t = "Please enter the subject name!"
            text_to_speech(t)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read(trainimagelabel_path)
                except:
                    """e = "Model not found, please train model"
                    Notifica.configure(
                        text=e,
                        width=33,
                    )
                    Notifica.place(x=20, y=250)
                    text_to_speech(e)"""
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Enrollment", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y: y + h, x: x + w])
                        if conf < 70:
                            print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime(
                                "%Y-%m-%d"
                            )
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                                "%H:%M:%S"
                            )
                            aa = df.loc[df["Enrollment"] == Id]["Name"].values
                            global tt
                            tt = str(Id) + "-" + aa
                            # En='1604501160'+str(Id)
                            attendance.loc[len(attendance)] = [
                                Id,
                                aa,
                            ]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                            )
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(
                        ["Enrollment"], keep="first"
                    )
                    cv2.imshow("Filling Attendance...", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:
                        break

                ts = time.time()
                print(aa)
                # attendance["date"] = date
                # attendance["Attendance"] = "P"
                attendance[date] = 1
                date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour, Minute, Second = timeStamp.split(":")
                # fileName = "Attendance/" + Subject + ".csv"
                path = os.path.join(attendance_path, Subject)
                fileName = (
                        f"{path}/"
                        + Subject
                        + "_"
                        + date
                        + "_"
                        + Hour
                        + "-"
                        + Minute
                        + "-"
                        + Second
                        + ".csv"
                )
                attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
                print(attendance)
                attendance.to_csv(fileName, index=False)

                m = "Attendance Filled Successfully of " + Subject
                """Notifica.configure(
                    text=m,
                    width=33,
                    relief=RIDGE,
                )
                text_to_speech(m)

                Notifica.place(x=20, y=250)"""

                cam.release()
                cv2.destroyAllWindows()

                import csv
                import tkinter

                root = tkinter.Tk()
                root.title("Attendance of " + Subject)
                root.configure(background="black")
                cs = os.path.join(path, fileName)
                print(cs)
                with open(cs, newline="") as file:
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
                print(attendance)
            except:
                f = "No Face found for attendance"
                text_to_speech(f)
                cv2.destroyAllWindows()

    ###windo is frame for subject chooser
    subject = Tk()
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
    # window.iconbitmap("AMS.ico")
    subject.title("Take Attendance")
    subject.geometry("500x200")
    subject.configure(background=darksem)
    subject.resizable(0, 0)
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = ttk.Label(
        subject,
        text="Enter the Subject Name",
        font=("arial", 25),
    )
    titl.place(relx=0.5, rely=0.1, anchor=CENTER)

    """Notifica = ttk.Label(
        subject,
        text="Attendance filled Successfully",
        width=33,
    )
    Notifica.place(relx=0.1, rely=0.25, anchor=W)"""

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

    fill_a = ttk.Button(
        subject,
        text="Fill Attendance",
        command=FillAttendance,
        width=18,
    )
    fill_a.place(relx=0.33, rely=0.7, anchor=CENTER)
    subject.mainloop()
