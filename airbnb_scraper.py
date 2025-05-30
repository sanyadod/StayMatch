from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_airbnb(location, checkin, checkout, max_pages=5):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    listings = []

    for page in range(1, max_pages + 1):
        url = f"https://www.airbnb.com/s/{location}/homes?checkin={checkin}&checkout={checkout}&items_offset={(page-1)*20}"
        driver.get(url)
        time.sleep(5)  # Wait for page to load
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for listing in soup.select('div[itemprop="itemListElement"]'):
            title = listing.select_one('meta[itemprop="name"]')
            price = listing.select_one('span[class*="price"]')
            address = listing.select_one('div[class*="location"]')
            if title and price and address:
                listings.append({
                    'title': title['content'],
                    'price': price.get_text(strip=True),
                    'address': address.get_text(strip=True)
                })
    driver.quit()
    return pd.DataFrame(listings)
