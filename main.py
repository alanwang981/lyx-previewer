import os, webbrowser
# get functions from other files
from convert import lyx_to_html
import frontend, getfile

def preview(file_ID):
    try: 
        # create a folder and path for files to be stored in
        save_folder = os.path.abspath("saved_files") 
        os.makedirs(save_folder, exist_ok=True)
        lyx_file = os.path.join(save_folder, "file.lyx")

        # download the file from google drive
        getfile.download_drive_file(file_ID, lyx_file)
        # only run the rest if script has permission to file
        if getfile.has_perm: 
            # convert the lyx file to html
            lyx_to_html(lyx_file)
            html_path = lyx_file.replace(".lyx", ".html")

            # open the html file in browser
            if html_path and os.path.exists(html_path):
                webbrowser.open(f"file://{html_path}")
                frontend.result_label.config(text="Preview opened!")
            else:
                frontend.displayError("Conversion failed or HTML file not found.")

    except Exception as e:
        frontend.displayError(e)

if __name__ == "__main__":

    frontend.launch_gui() # launch the GUI for the program
