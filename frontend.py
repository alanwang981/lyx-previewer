import tkinter, re

def launch_gui():

    # create the GUI window
    root = tkinter.Tk()
    root.title("LyX-Previewer")
    root.geometry("500x300")

    # add the URL input widget
    tkinter.Label(root, text="Paste Google Drive URL here:").pack(pady=5)
    global url_entry
    url_entry = tkinter.Entry(root, width=60)
    url_entry.pack(pady=5)

    # add button that launches preview
    preview_button = tkinter.Button(root, text="Preview File", command=extract_file_id)
    preview_button.pack(pady=10)

    # label to show result
    global result_label
    result_label = tkinter.Label(root, text="Waiting for input...")
    result_label.pack(pady=10)

    # run the GUI loop
    root.mainloop()

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