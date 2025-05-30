from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

def scrape_apartments(location, max_pages=5):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    listings = []

    for page in range(1, max_pages + 1):
        url = f"https://www.apartments.com/{location}/?page={page}"
        driver.get(url)
        time.sleep(3)  # Wait for page to load
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for listing in soup.select('.placard'):
            title = listing.select_one('.property-title')
            price = listing.select_one('.property-pricing')
            address = listing.select_one('.property-address')
            if title and price and address:
                listings.append({
                    'title': title.get_text(strip=True),
                    'price': price.get_text(strip=True),
                    'address': address.get_text(strip=True)
                })
    driver.quit()
    return pd.DataFrame(listings)
