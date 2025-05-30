from apify_client import ApifyClient
import pandas as pd

def scrape_furnishedfinder(api_token, start_url):
    client = ApifyClient(api_token)
    run_input = {
        "startUrls": [{"url": start_url}],
        "proxy": {"useApifyProxy": True}
    }
    run = client.actor("memo23/furnishedfinder-scraper-cheerio").call(run_input=run_input)
    listings = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        listings.append(item)
    return pd.DataFrame(listings)
