from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.documents
collection = db['pdf_texts']

# Query the document with title "2021-RCHSD-Audit-Report"
document = collection.find_one({"title": "2021-RCHSD-Audit-Report"})

# Check if the document exists and print the text
if document:
    print(f"Text from '2021-RCHSD-Audit-Report':\n")
    print(document['text'])
else:
    print("Document not found.")

# Close MongoDB connection
client.close()