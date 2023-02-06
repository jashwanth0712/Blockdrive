from tkinter import *
from tkinter import ttk
import time


def update_progress(value):
    progress_bar["value"] = value
    window.update()


def your_time_consuming_function():
    print("Starting function")
    update_progress(0)
    time.sleep(2)
    print("I reached my first checkpoint")
    update_progress(25)
    time.sleep(2)
    print("Another checkpoint, yay")
    update_progress(50)
    time.sleep(2)
    print("Only 1 more to go")
    update_progress(75)
    time.sleep(2)
    print("Yay im finished")
    update_progress(100)


window = Tk()
#Set title
window.title ('installing')
# Set window size
window.geometry("800x500")
# add logo
# window.iconbitmap('logo.ico')
label = ttk.Label(window, text="Installing Required files", font=("Helvetica", 20))
label.pack(pady=20)
progress_bar = ttk.Progressbar(window, length=500, mode="determinate", orient="horizontal")
progress_bar.grid(row=99, column=0, sticky=E, padx=100, pady=2)

your_time_consuming_function()
window.mainloop()