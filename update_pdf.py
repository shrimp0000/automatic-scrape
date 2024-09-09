import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def download_new_pdf(chrome_driver_path, pdf_urls):
    # Path to your ChromeDriver
    # chrome_driver_path = r'C:\Users\sebas\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

    # Set up ChromeDriver with download preferences
    chrome_options = Options()
    output_dir_name = 'output_pdfs'
    download_folder = os.path.join(os.getcwd(), output_dir_name)
    os.makedirs(download_folder, exist_ok=True)
    chrome_prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    for url in pdf_urls:
        driver.get(url)
        
        # Give the page time to load
        time.sleep(5)
