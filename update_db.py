from pymongo import MongoClient
import os
import PyPDF2

def insert_into_db(files_to_be_insert, output_directory):
    cluster = "mongodb://localhost:27017/"
    client = MongoClient(cluster)

    print(client.list_database_names())

    db = client.documents
    collection_name = 'pdf_texts'
    if collection_name not in db.list_collection_names():
        db.command("create", collection_name)
    collection = db[collection_name]

    for pdf_name in files_to_be_insert:
        # Construct the full path to the PDF file
        pdf_path = os.path.join(output_directory, pdf_name)
        
        # Open the PDF file
        if pdf_name.endswith('.pdf'):
            with open(pdf_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                
                # Initialize a string to store the extracted text
                full_text = ""

                # Iterate through each page in the PDF
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    full_text += text + "\n"

            # Store the extracted text in MongoDB
            document = {
                "title": pdf_name.replace('.pdf', ''),
                "text": full_text
            }
            collection.insert_one(document)

            print(f'Stored text from {pdf_name} in MongoDB')

    # Close MongoDB connection
    client.close()