import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

from gtts import gTTS

import automaticAttedance
# project module
import show_attendance
import takeImage
import trainImage


# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    gTTS(user_text)
    """engine = pyttsx.init()
    engine.say(user_text)
    engine.runAndWait()"""


haarcasecade_path = "/home/manjaro/Downloads/face_reco/haarcascade_frontalface_default.xml"
trainimagelabel_path = "/home/manjaro/Downloads/face_reco/TrainingImageLabel/Trainner.yml"
trainimage_path = "/home/manjaro/Downloads/face_reco/TrainingImage"
studentdetail_path = "/home/manjaro/Downloads/face_reco/StudentDetails/studentdetails.csv"
attendance_path = "/home/manjaro/Downloads/face_reco/Attendance"

darksem = "#252526"

window = Tk()

# tell tcl where to find the awthemes packages
window.tk.eval("""
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
window.tk.call("package", "require", 'awdark')
window.tk.call("package", "require", 'awlight')

s = ttk.Style(window)
s.theme_use('awdark')
window.title("DIY Attendance")
window.geometry("260x290")
window.resizable(0, 0)
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background=darksem)

"""frameA = tk.Frame()
frameA.pack(side='top', fill=None)"""


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = ttk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    ttk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        # fg="yellow",
        # bg="black",
        font=("times", 20, " bold "),
    ).pack()
    ttk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        # fg="yellow",
        # bg="black",
        width=9,
        # height=1,
        # activebackground="Red",
        # font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


a = ttk.Label(
    window,
    text="IIT KGP Face Attendance Check",
    # bg=darksem,
    # fg="yellow",
    # bd=10,
    font=("Arial", 35),
    # style='hFont',
)
a.place(relx=0.5, rely=0.15, anchor=CENTER)
"""
ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)
"""


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.tk.eval("""
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
    ImageUI.tk.call("package", "require", 'awdark')
    ImageUI.tk.call("package", "require", 'awlight')

    imageUI = ttk.Style(ImageUI)
    imageUI.theme_use('awdark')
    ImageUI.configure(background=darksem)
    ImageUI.title("Take Student Image")
    ImageUI.geometry("540x300")
    ImageUI.resizable(0, 0)

    # image and title
    titl = ttk.Label(
        ImageUI, text="Register Your Face",
        font=("arial", 30),
    )
    titl.place(relx=0.5, rely=0.05, anchor=CENTER)

    # heading
    a = ttk.Label(
        ImageUI,
        text="Enter the details:-",
        # bg="black",
        # fg="yellow",
        # bd=10,
        font=("arial", 24),
    )
    a.place(relx=0.22, rely=0.2, anchor=CENTER)

    # ER no
    lbl1 = ttk.Label(
        ImageUI,
        text="Enrollment No.:",
        width=15,
        # height=2,
        # bg="black",
        # fg="yellow",
        # bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(relx=0.14, rely=0.36, anchor=W)
    txt1 = ttk.Entry(
        ImageUI,
        width=18,
        # bd=5,
        validate="key",
        # bg="black",
        # fg="yellow",
        # relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(relx=0.38, rely=0.36, anchor=W)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = ttk.Label(
        ImageUI,
        text="Name:",
        width=15,
        # height=2,
        # bg="black",
        # fg="yellow",
        # bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(relx=0.14, rely=0.46, anchor=W)
    txt2 = ttk.Entry(
        ImageUI,
        width=18,
        # bd=5,
        # bg="black",
        # fg="yellow",
        # relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(relx=0.38, rely=0.46, anchor=W)

    lbl3 = ttk.Label(
        ImageUI,
        text="Notification:",
        width=15,
        # height=2,
        # bg="black",
        # fg="yellow",
        # bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(relx=0.14, rely=0.56, anchor=W)

    # messagey = 0.56 #0.58
    message = ttk.Label(
        ImageUI,
        text="",
        width=32,
        # height=2,
        # bd=5,
        # bg="black",
        # fg="yellow",
        relief=RIDGE,
        font=("times new roman", 12, "bold"),
    )
    message.place(relx=0.38, rely=0.56, anchor=W)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = ttk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        width=12,
    )
    takeImg.place(relx=0.34, rely=0.8, anchor=CENTER)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = ttk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        width=12,
    )
    trainImg.place(relx=0.64, rely=0.8, anchor=CENTER)


r = ttk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    width=25,
)
r.place(relx=0.5, rely=0.4, anchor=CENTER)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = ttk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    width=25,
)
r.place(relx=0.5, rely=0.6, anchor=CENTER)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = ttk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    width=25,
)
r.place(relx=0.5, rely=0.8, anchor=CENTER)
"""
r = ttk.Button(
    window,
    text="EXIT",
    #bd=10,
    command=quit,
    #font=("times new roman", 16),
    #bg="black",
    #fg="yellow",
    #height=2,
    width=20,
)
r.place(x=600, y=660)
"""

window.mainloop()
