first time scraping a website:\
run in order:\
    scrape_from_web.py - generate pdf_links.txt, which has all the links of the pdf (scraped from the web) to be downloaded;\
    scrape_pdf.py - generate directory output_pdfs, download all the pdf following pdf_links into it;\
    save_txt_to_db.py - read all pdf text and save them into MongoDB database;\

checking if there is any updates of a website:\
run:\
    check_web_updates.py - find new pdf links, record in pdf_links.txt, download the pdfs, save in database.\

check_web_updates.py can be run in a daily basis, or in any time interval to check for updates of a website. After setting its running frequency, it can be easily automated, such as using Bash commands.

