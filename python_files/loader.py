import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess 

def next_func():
    print("Next button clicked")
   
    subprocess.call(["python", "./Registry handler/register.py"])
    subprocess.call(["python", "./Registry handler/register1.py"])
    root.destroy()
    subprocess.call(["python", "./toolchain.py"])
   

    

def cancel_func():
    print("Cancel button clicked")
    root.destroy()

root = tk.Tk()
root.title("Installation Page")
root.geometry("500x400")
image = Image.open(r'C:\Users\jashw\OneDrive\Documents\projects\fvm\Blockdrive\logo.png')
image = image.resize((200, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
label = tk.Label(root)
label.config(image=image)
label.image = image
label.pack()

label = tk.Label(root, text="Welcome to the installation page", font=("Helvetica", 20))
label.pack(pady=20)

description = tk.Label(root, text="This page will guide you through the installation process.", font=("Helvetica", 14))
description.pack()
description = tk.Label(root, text=" Click 'Next' to continue or 'Cancel' to exit.", font=("Helvetica", 14))
description.pack()

next_button = tk.Button(root, text="Next", command=next_func)
next_button.pack(padx=25,side="right")

cancel_button = tk.Button(root, text="Cancel", command=cancel_func)
cancel_button.pack(padx=25,side="left")

root.mainloop()
