import subprocess
import os

def lyx_to_pdf(lyx_file):
    # Step 1: Get absolute paths
    lyx_path = "C:/Program Files/LyX 2.4/bin/LyX.exe"  # Windows

    # Convert to absolute paths
    # lyx_path = os.path.normpath(lyx_path)  # Normalize path
    # lyx_file = os.path.abspath(lyx_file)   # Full path to .lyx file

    # Debug: Check if paths exist
    print("LyX exists:", os.path.exists(lyx_path))
    print("LyX file exists:", os.path.exists(lyx_file))

    try:
        # Run LyX
        subprocess.run(
            [lyx_path, "-e", "pdf2", lyx_file],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("Conversion successful!")
        pass
    except subprocess.CalledProcessError as e:
        print("ERROR:", e.stderr)
    except FileNotFoundError:
        print("LyX not found at:", lyx_path)

lyx_to_pdf("C:/test/MCM45 Class 10 Instructor.lyx")


'''
"C:/Program Files/LyX 2.4/bin/LyX.exe" -e pdf2 "C:/test/test1.lyx"
"C:/Program Files/LyX 2.4/bin/LyX.exe"
"C:/test/test1.lyx"
'''