from tkinter import *
from tkinter import messagebox
import time
import pyttsx3
from win11toast import toast

pressedOkButton = False


def remainderNotify() :
    global hh_spin, mm_spin, ss_spin, pressedOkButton, remainderEntry, root

    engine = pyttsx3.init()

    # change the speed of the engine
    engine.setProperty("rate", 150)

    hours = int(hh_spin.get())
    minutes = int(mm_spin.get())
    seconds = int(ss_spin.get())

    print(hours, minutes, seconds)

    if (pressedOkButton == False) :
        messagebox.showerror("Press OK", "Please press Ok button, after giving Reminder")

    elif (seconds == "0" and hours == "0" and minutes == "0"):
        messagebox.showerror("Select Time", "Please enter a valid time for the reminder")
    
    else:
        msg = "Sir, you have a reminder, which is named as " + remainderEntry.get()
        messagebox.showinfo(title = "Reminder Set", message = "Reminder Set Successfully!!")

        root.destroy()

        # execute the program after the given time
        time.sleep(hours*3600 + minutes*60 + seconds)
        
        engine.say(msg)
        engine.runAndWait()
        toast("Reminder App", msg, button = "Mark as Done")

def reminder() :
    global pressedOkButton
    pressedOkButton = True
    if (remainderEntry.get() == "" and pressedOkButton) :
        messagebox.showerror("Empty Reminder", "Please enter the name of reminder")
        pressedOkButton = False
    

root = Tk()
root.title("Remainder-App")
root.geometry("400x450+400+100")
root.resizable(False, False)

# icon for the app
imageIcon = PhotoImage(file = "D:/College/HIT/Mini Project (3rd Year)/Reminder App/img/remainder_icon.png")
root.iconphoto(False, imageIcon)

# heading label for the app
heading = Label(root, text = "Remainder App", font = "arial 20 bold", fg = "white", bg = "#32405b")
heading.place(x = 100, y = 20)

# Remainder label
remainderLabel = Label(root, text = "What's the remainder to remind about?", font = "lato 14 bold")
remainderLabel.place(x = 30, y = 75)

# remainder entry content
frame = Frame(root, width = 400, height = 50, bg = "white")
frame.place(x = 0, y = 110)

# Entry remainder
remainderEntry = Entry(frame, width = 18, font = "arial 20", bd = 0)
remainderEntry.place(x = 10, y = 7)
remainderEntry.focus()

# Button to set remainder name
okButton = Button(frame, text = "OK", font = "arial 20 bold", width = 6, bg = "#5a95ff", fg = "white", bd = 0, command = reminder)
okButton.place(x = 300, y = 0)

# Set Time label
setTimeLabel = Label(root, text = "Remind me in", font = "lato 14 bold")
setTimeLabel.place(x = 140, y = 180)

# time entry content
timeFrame = Frame(root, width = 400, height = 50, bg = "white")
timeFrame.place(x = 0, y = 210)

# time entry
hh_spin = Spinbox(timeFrame, from_ = 0, to = 12, width = 3, font = "arial 16", bd = 1)
hh_spin.place(x = 10, y = 7)
Label(timeFrame, text = "HR", font = "arial 16").place(x = 80, y = 7)

mm_spin = Spinbox(timeFrame, from_ = 0, to = 59, width = 3, font = "arial 16", bd = 1)
mm_spin.place(x = 130, y = 7)
Label(timeFrame, text = "MIN", font = "arial 16").place(x = 200, y = 7)

ss_spin = Spinbox(timeFrame, from_ = 0, to = 59, width = 3, font = "arial 16", bd = 1)
ss_spin.place(x = 250, y = 7)
Label(timeFrame, text = "SEC", font = "arial 16").place(x = 320, y = 7)

# Reminder button
reminderButton = Button(root, bg = "red", fg = "white", text = "SET REMINDER", font = "arial 20 bold", bd = 5, command = remainderNotify)
reminderButton.place(x = 80, y = 280)

root.mainloop()