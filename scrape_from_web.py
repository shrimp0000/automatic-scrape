from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

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

# start from the 1st element because there is a file in the beginning with the same title which shouldn't be used
output_file_path = 'pdf_links.txt'

with open(output_file_path, 'w') as file:
    for link in matching_links[1:]:
        # full pdf url
        pdf_url = start_string + link
        file.write(pdf_url + '\n')
    
# Close the browser
driver.quit()