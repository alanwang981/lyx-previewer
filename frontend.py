import tkinter
import keyboard
from main import preview

# Global variables
user_hotkey = "ctrl+alt+g"  # default hotkey
status_label = None

def launch_gui():

    # Create the GUI window
    root = tkinter.Tk()
    root.title("LyX-Previewer")
    root.geometry("300x150")

    # Create the user interaction button
    tkinter.Label(root, text="Click the button and press your hotkey:").pack(pady=5)
    tkinter.Button(root, text="Set Hotkey", command=set_hotkey).pack(pady=5)
    
    # Display for the current hotkey
    global status_label
    status_label = tkinter.Label(root, text="Default hotkey: ctrl+alt+g")
    status_label.pack(pady=10)

    # Register default hotkey
    register_hotkey()
    # Run the GUI loop
    root.mainloop()

def set_hotkey():
    global status_label
    global user_hotkey
    status_label.config(text="Press the hotkey combination now...")
    status_label.update()  # refresh the label to show the message
    user_hotkey = keyboard.read_hotkey(suppress=False)  # blocks until user presses a combination
    keyboard.unhook_all_hotkeys()  # remove previous hotkeys
    register_hotkey()
    status_label.config(text=f"Hotkey set to: {user_hotkey}") # update the display

def register_hotkey():
    global user_hotkey
    keyboard.add_hotkey(user_hotkey, preview) # add user_hotkey
