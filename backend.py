import subprocess

def lyx_to_pdf(lyx_file):
    lyx_path = "C:/Program Files/LyX 2.4/bin/LyX.exe"
    try:
        subprocess.run(
            [lyx_path, "-e", "pdf2", lyx_file],
            check = False,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True
        )
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print("ERROR:", e.stderr)
    except FileNotFoundError:
        print("LyX not found at:", lyx_path)
 
lyx_to_pdf("C:/test/MCM45 Class 10 Instructor.lyx")