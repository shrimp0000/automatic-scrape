from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os
from update_pdf import download_new_pdf
from update_db import insert_into_db

# Path to your ChromeDriver
chrome_driver_path = r'C:\Users\sebas\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Set up ChromeDriver
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Open the URL with Selenium
url = "https://www.dhcs.ca.gov/services/Pages/MedRevAuditsCAP.aspx"
driver.get(url)

# Give the page time to load
time.sleep(5)

# Get the page source and parse with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

prefix = "/services/Documents/MCQMD/Compliance%20Unit-CAP"

# Find all <a> elements with href attributes that start with the specified prefix
links = soup.find_all('a', href=True)
matching_links = [link['href'] for link in links if link['href'].startswith(prefix)]

start_string = "https://www.dhcs.ca.gov"
matching_links = [start_string + link for link in matching_links]

output_file_path = 'pdf_links.txt'

# get the original pdf file names to compare later
pdf_directory = 'output_pdfs'
old_pdf_file_names = os.listdir(pdf_directory)

with open(output_file_path, 'r+') as file:
    previous_pdf_urls = [line.strip() for line in file.readlines()]
    # matching_links[1:] - start from the 1st element because there is a file in the beginning with the same
    # title which shouldn't be used
    new_pdf_urls = [link for link in matching_links[1:] if link not in previous_pdf_urls]
    if new_pdf_urls:
        print(f"New PDF links found: {new_pdf_urls}")
        # Move the file pointer to the end before writing new links
        file.seek(0, 2)  # Move the pointer to the end of the file
        
        # write in new pdf link
        for link in new_pdf_urls:
            file.write(link + '\n')
            
        # download new pdf
        download_new_pdf(chrome_driver_path, new_pdf_urls)
        print("New PDF downloaded")
        
    else:
        print("No new PDF links found.")

if new_pdf_urls:
    new_pdf_file_names = os.listdir(pdf_directory)
    new_pdf_files_names_to_be_db = [pdf for pdf in new_pdf_file_names if pdf not in old_pdf_file_names]
    print(f"New PDF files: {new_pdf_files_names_to_be_db}")
    
    # insert new pdf text into database
    insert_into_db(new_pdf_files_names_to_be_db, pdf_directory)
    print("New PDF text inserted.")

    
# Close the browser
driver.quit()