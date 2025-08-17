import shutil
import os
import webbrowser
from threading import Thread
# get functions from other files
from getfile import download_drive_file
from convert import lyx_to_html
import frontend

def preview():
    try: 
        file_id = "1RSkXkKzzBn--_VCfiSbFAR6Qgq0e3QMM" # this needs to be automated later

        # delete intermediate files to clean up, if there are any
        save_folder = os.path.abspath("saved_files") # declare save_folder
        if os.path.exists(save_folder):
            shutil.rmtree(save_folder)
        
        # create a folder and path for files to be stored in
        save_folder = os.path.abspath("saved_files")
        os.makedirs(save_folder, exist_ok=True)
        lyx_file = os.path.join(save_folder, "file.lyx")

        # download the file from google drive
        download_drive_file(file_id, lyx_file)

        # convert the lyx file to html
        lyx_to_html(lyx_file)
        html_path = lyx_file.replace(".lyx", ".html")

        # attempt to open the html file in browser
        if html_path and os.path.exists(html_path):
            webbrowser.open(f"file://{html_path}")
        else:
            print("Conversion failed or HTML file not found.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    Thread(target=frontend.hotkey, daemon=True).start() # start listening for hotkey
    frontend.launch_gui() # launch the gui for customizing hotkey
