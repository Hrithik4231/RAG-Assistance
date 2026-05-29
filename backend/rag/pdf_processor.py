import os
from PyPDF2 import PdfReader

UPLOAD_FOLDER = "uploads"

def extract_text_from_pdfs():

    all_text = ""
    for filename in os.listdir(UPLOAD_FOLDER): # Loop through all files in the uploads directory
        if filename.endswith(".pdf"):

            pdf_path = os.path.join(UPLOAD_FOLDER, filename)
            reader = PdfReader(pdf_path) # PDFreader -  opens PDF file and allows us to read its content
            print(f"\nProcessing : {filename}")

            for page in reader.pages: #loop through all the pages in the PDF and extract text from each page
                text = page.extract_text()

                if text:
                    all_text += text + "\n"

    return all_text

def chunk_text(text, chunk_size=300, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


