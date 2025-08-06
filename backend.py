import subprocess
import os
from spire.pdf import PdfDocument
from spire.pdf import FileFormat

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
    except subprocess.CalledProcessError as e:
        print("ERROR:", e.stderr)
    except FileNotFoundError:
        print("LyX not found at:", lyx_path)
        
def pdf_to_html(pdf_file):
    doc = PdfDocument()
    doc.LoadFromFile(pdf_file)
    convertOptions = doc.ConvertOptions
    convertOptions.SetPdfToHtmlOptions(True, True, 1, True)
    doc.SaveToFile(pdf_file.replace(".pdf", ".html"), FileFormat.HTML)
    doc.Dispose()

def lyx_to_html(file_name):
    if not os.path.exists(file_name):
        print("File does not exist!")
        return
    lyx_to_pdf(file_name)
    pdf_to_html(file_name.replace(".lyx", ".pdf"))
    os.remove(file_name.replace(".lyx", ".pdf"))
    
lyx_to_html("ME35 Homework 10 Solutions.lyx")