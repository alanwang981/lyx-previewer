import shutil
import os
import webbrowser
# get functions from other files
from getfile import download_drive_file
from convert import lyx_to_html

def main():
    try: 
        file_id = "1RSkXkKzzBn--_VCfiSbFAR6Qgq0e3QMM" # this needs to be automated later
        
        # create a folder and path for files to be stored in
        save_folder = os.path.abspath("saved_files")
        os.makedirs(save_folder, exist_ok=True)
        lyx_file = os.path.join(save_folder, "file.lyx")

        # download the file from google drive
        print("Downloading file...")
        download_drive_file(file_id, lyx_file)
        print(f"Downloaded file to: {lyx_file}")

        # convert the lyx file to html
        print("Converting to HTML...")
        lyx_to_html(lyx_file)
        html_path = lyx_file.replace(".lyx", ".html")

        # attempt to open the html file in browser
        if html_path and os.path.exists(html_path):
            print("Opening HTML in browser...")
            webbrowser.open(f"file://{html_path}")
        else:
            print("Conversion failed or HTML file not found.")

        # delete intermediate files to clean up
        if os.path.exists(save_folder):
            shutil.rmtree(save_folder)
            print(f"Deleted folder {save_folder}")

    except Exception as e:
        print("Error:", e)
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
