import subprocess
from frontend import displayError

# this function converts the lyx to xhtml when given the file path of the lyx file
def lyx_to_xhtml(lyx_file):
    lyx_path = "C:/Program Files/LyX 2.4/bin/LyX.exe"
    try:
        subprocess.run(
            [lyx_path, "-e", "xhtml", lyx_file],
            check = False,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = False
        )
    except subprocess.CalledProcessError as e:
        displayError(str(e.stderr))
    except FileNotFoundError:
        displayError("LyX not found at: "+lyx_path)