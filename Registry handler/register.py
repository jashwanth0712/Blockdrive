import winreg
import sys
import os
import webbrowser

def open_url(url):
    webbrowser.open_new_tab(url)

# def rename_to_hi(file_path):
#     open_url("www."+"\"%1\"")
#     print(os.path(sys.argv[1]))
#     a=input()
#     os.rename(file_path, os.path.join(os.path.dirname(file_path), "Upload to Blockdrive"))

def add_context_menu_entry():
    try:
        reg_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\shell\run")
        winreg.SetValue(reg_key, "", winreg.REG_SZ, "Upload to Blockdrive")
        command_key = winreg.CreateKey(reg_key, r"command")
        winreg.SetValue(command_key, '', winreg.REG_SZ, r'C:\Users\jashw\OneDrive\Documents\projects\fvm\Blockdrive\Registry handler\handler.exe')
        winreg.SetValueEx(reg_key, 'Icon', 0, winreg.REG_SZ, r'C:\Users\jashw\OneDrive\Documents\projects\fvm\Blockdrive\Registry handler\icon.ico') 
        # winreg.SetValue(command_key, "", winreg.REG_SZ, sys.executable + " -c \"from subprocess import *;Popen('python C:\\Users\\jashw\\OneDrive\\Documents\\projects\\practice\\python\\modification handler\\webopen.py sys.argv[1]')\"\"%1\"")
        # winreg.SetValue(command_key, "", winreg.REG_SZ, sys.executable + " -c \"import os, sys; os.rename(sys.argv[1], os.path.join(os.path.dirname(sys.argv[1]), 'hi'))\" \"%1\"")
    except WindowsError as e:
        print("Error adding context menu entry:", e)

if __name__ == "__main__":
    print("installing reg1")
    add_context_menu_entry()
