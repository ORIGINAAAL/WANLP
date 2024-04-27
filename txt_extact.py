from flask import Flask, request
import os
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader
import easyocr

app = Flask(__name__)

# from Picture to Text 
def text_recognition(filename):
    reader = easyocr.Reader(['ar'])
    results = reader.readtext(os.path.join('/path/to/save', filename), detail = 1)
    sorted_results = sorted(results, key=lambda result: result[0][0][1])
    all_words = [result[1] for result in sorted_results]
    text = ' '.join(all_words)
    return text

# from pdf to text
def pdf_reader(filename):
    reader = PdfFileReader(os.path.join('/path/to/save', filename)) 
    all_pages_text = []
    for page_number in range(len(reader.pages)):
        page_text = reader.pages[page_number].extract_text()
        all_pages_text.append(page_text)

    all_text = ' '.join(all_pages_text)
    return all_text

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('/path/to/save', filename))
    
    # Check if the file is an image or a PDF
    if filename.endswith('.pdf'):
        text = pdf_reader(filename)
    else:
        text = text_recognition(filename)
        
    return text

if __name__ == '__main__':
    app.run(debug=True)