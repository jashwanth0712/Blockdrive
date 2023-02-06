import winreg
import sys
import os
import webbrowser

def open_url(url):
    webbrowser.open_new_tab(url)


def add_context_menu_entry():
    try:
        reg_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\j")
        winreg.SetValue(reg_key, "", winreg.REG_SZ, "View on lighthouse")
        command_key = winreg.CreateKey(reg_key, r"command")
        winreg.SetValue(command_key, '', winreg.REG_SZ, r'C:\Users\jashw\OneDrive\Documents\projects\fvm\Blockdrive\Registry handler\webpage_open.exe')
        winreg.SetValueEx(reg_key, 'Icon', 0, winreg.REG_SZ, r'C:\Users\jashw\OneDrive\Documents\projects\fvm\Blockdrive\Registry handler\lighthouse.ico') 
        # winreg.SetValue(command_key, "", winreg.REG_SZ, sys.executable + " -c \"from subprocess import *;Popen('python C:\\Users\\jashw\\OneDrive\\Documents\\projects\\practice\\python\\modification handler\\webopen.py sys.argv[1]')\"\"%1\"")
        # winreg.SetValue(command_key, "", winreg.REG_SZ, sys.executable + " -c \"import os, sys; os.rename(sys.argv[1], os.path.join(os.path.dirname(sys.argv[1]), 'hi'))\" \"%1\"")
    except WindowsError as e:
        print("Error adding context menu entry:", e)

if __name__ == "__main__":
    add_context_menu_entry()
