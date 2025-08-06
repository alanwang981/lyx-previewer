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

def clean_html(html_file):
    warning = (
        "<tspan xml:space=\"preserve\" style=\"white-space: pre;\" x=\"20\" y=\"20\" "
        "font-family=\"Arial\" font-weight=\"normal\" font-style=\"normal\" font-size=\"10\" "
        "fill=\"#ff0000\">Evaluation Warning : The document was created with Spire.PDF for Python.</tspan>"
    )
     
    def insertAfter(haystack, needle, newText):
        idx = haystack.find(needle)
        return haystack[:idx + len(needle)] + newText + haystack[idx + len(needle):]

    def insertBefore(haystack, needle, newText):
        idx = haystack.find(needle)
        return haystack[:idx] + newText + haystack[idx:]
    
    with open(html_file, "r", encoding = 'utf-8') as file:
        content = file.read()
        content = content.replace(warning, "")
        
        content = insertAfter(content, "</title>", "<style>body{text-align:center;}.centered{margin:auto;width:50%;text-align:center;}</style>")
        content = insertAfter(content, "<body style='margin:0'>", "<div class='centered'>")
        content = insertBefore(content, "</body>", "</div>")
    
    with open(html_file, "w", encoding = 'utf-8') as file:
        file.write(content)
    
def lyx_to_html(file_name):
    if not os.path.exists(file_name):
        print("File does not exist!")
        return
    lyx_to_pdf(file_name)
    pdf_to_html(file_name.replace(".lyx", ".pdf"))
    os.remove(file_name.replace(".lyx", ".pdf"))
    clean_html(file_name.replace(".lyx", ".html"))
    
lyx_to_html("ME35 Homework 10 Solutions.lyx")