# convert pdf to txt

import os
import PyPDF2

# Path to the output directory
pdf_directory = 'output_pdfs'
txt_output_directory = 'output_txts'
os.makedirs(txt_output_directory, exist_ok=True)

# Get all file names in the directory
file_names = os.listdir(pdf_directory)

for pdf_name in file_names:
    # Open the PDF file
    pdf_path = os.path.join(pdf_directory, pdf_name)
    
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Initialize a string to store the extracted text
        full_text = ""

        # Iterate through each page in the PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            full_text += text + "\n"

    # Write the extracted text to a file
    output_file_path = os.path.join(txt_output_directory, pdf_name.replace('.pdf', '.txt'))
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(full_text)
