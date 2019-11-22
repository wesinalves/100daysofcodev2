# Python Journey - Chapter 24
# Combines all the PDFs in the current working directory into a single file

import PyPDF2, os

# Get all the PDF filenames.
pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdfFiles.sort(key/str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Loop through all the PDF files.
# TODO: Loop through all the pages (except the first) and add them.
# TODO: Save the resulting PDF to a file.
