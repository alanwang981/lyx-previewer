from sysconfig import get_path
import tkinter as tk, re
    
url_placeholder = "https://drive.google.com/..."
root = tk.Tk()
    
TITLE_FONT = ("Segoe UI", 16, "bold")
LABEL_FONT = ("Segoe UI", 11)
BUTTON_FONT = ("Segoe UI", 10, "bold")

def launch_gui():

    # create the GUI window
    root.title("LyX Previewer")
    root.geometry("500x250")
    root.configure(bg="#f5f5f5")
    root.iconbitmap("icon.ico")

    # add the URL input title and subtitle
    tk.Label(root, text="LyX File Previewer", font=TITLE_FONT, bg="#f5f5f5").pack(pady=(20, 10))
    tk.Label(root, text="Paste Google Drive URL here:",font=LABEL_FONT, bg="#f5f5f5").pack()
    
    # add url entry
    global url_entry
    url_entry = tk.Entry(root, width=50, font=("Segoe UI", 10), relief="solid", bd=1)
    url_entry.insert(0, url_placeholder)
    url_entry.config(fg="gray")
    url_entry.bind("<FocusIn>", clear_placeholder)
    url_entry.bind("<FocusOut>", add_placeholder)
    url_entry.bind("<Return>", lambda event: extract_file_id())
    url_entry.pack(pady=10, ipady=5)
    
    # add button that launches preview
    def on_enter(event):
        preview_button.config(bg="#3b7bd4")

    def on_leave(event):
        preview_button.config(bg="#4a90e2")
    preview_button = tk.Button(root, text="Preview File", font=BUTTON_FONT, bg="#4a90e2", fg="white", activebackground="#357ABD", relief="flat", padx=12, pady=6, command=extract_file_id)
    preview_button.pack(pady=(5, 10))
    preview_button.bind("<Enter>", on_enter)
    preview_button.bind("<Leave>", on_leave)

    # label to show result
    global result_label
    result_label = tk.Label(root, text="Waiting for input...", font=LABEL_FONT, bg="#f5f5f5", fg="#555")
    result_label.pack(pady=(5, 0))

    # run the GUI loop
    root.mainloop()

# clears and adds placeholder text to url entry
def clear_placeholder(event):
    if url_entry.get() == url_placeholder:
        url_entry.delete(0, tk.END)
        url_entry.config(fg="black")

def add_placeholder(event):
    if not url_entry.get():
        url_entry.insert(0, url_placeholder)
        url_entry.config(fg="gray")

def set_message(message):
    result_label.config(text=message, foreground="#333")
    root.update()

def extract_file_id():
    global file_ID
    url = url_entry.get().strip()
    match = re.search(r"(?:/d/|id=)([a-zA-Z0-9_-]+)", url)
    if match:
        # delayed import to avoid circular dependency
        from main import preview
        file_ID = match.group(1)
        preview(file_ID)
        url_entry.delete(0, tk.END)
        root.focus_set()
    else:
        file_ID = None
        result_label.config(text="Please enter a valid URL.", foreground="red")

def displayError(err):
    result_label.config(text="Error: " + str(err), foreground="red")