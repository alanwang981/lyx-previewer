import tkinter, re
    
url_placeholder = "https://drive.google.com/..."
root = tkinter.Tk()
    

def launch_gui():

    # create the GUI window
    root.title("LyX-Previewer")
    root.geometry("500x250")
    root.configure(bg="#f5f5f5")
    
    TITLE_FONT = ("Segoe UI", 16, "bold")
    LABEL_FONT = ("Segoe UI", 11)
    BUTTON_FONT = ("Segoe UI", 10, "bold")

    # add the URL input widget
    tkinter.Label(root, text="LyX File Previewer", font=TITLE_FONT, bg="#f5f5f5").pack(pady=(20, 10))

    tkinter.Label(root, text="Paste Google Drive URL here:",font=LABEL_FONT, bg="#f5f5f5").pack()
    
    # add url entry placehodler
    global url_entry
    url_entry = tkinter.Entry(root, width=50, font=("Segoe UI", 10))
    url_entry.insert(0, url_placeholder)
    url_entry.config(fg="gray")
    url_entry.bind("<FocusIn>", clear_placeholder)
    url_entry.bind("<FocusOut>", add_placeholder)
    url_entry.pack(pady=10, ipady=5)

    # add button that launches preview
    preview_button = tkinter.Button(root, text="Preview File", font=BUTTON_FONT, bg="#4a90e2", fg="white",
                           activebackground="#357ABD", relief="flat", padx=10, pady=5, command=extract_file_id)
    preview_button.pack(pady=(5, 10))

    # label to show result
    global result_label
    result_label = tkinter.Label(root, text="Waiting for input...", font=LABEL_FONT, bg="#f5f5f5", fg="#555")
    result_label.pack(pady=(10, 0))

    # run the GUI loop
    root.mainloop()

def clear_placeholder(event):
    if url_entry.get() == url_placeholder:
        url_entry.delete(0, tkinter.END)
        url_entry.config(fg="black")

def add_placeholder(event):
    if not url_entry.get():
        url_entry.insert(0, url_placeholder)
        url_entry.config(fg="gray")

def extract_file_id():
    global file_ID
    url = url_entry.get().strip()
    match = re.search(r"(?:/d/|id=)([a-zA-Z0-9_-]+)", url)
    if match:
        file_ID = match.group(1)
        from main import preview
        preview(file_ID)
    else:
        file_ID = None
        displayError("Not a valid Google Drive URL")

def displayError(err):
    global result_label
    result_label.config(text="Error: "+err)