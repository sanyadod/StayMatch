# AI-Powered Short-Term Housing Recommender

This is a Python-based data scraping and recommendation system designed to help students and professionals find short-term, furnished housing for internships or relocations. It scrapes apartment listings from multiple platforms including **Apartments.com**, **Airbnb**, and **Furnished Finder**, processes the listings, and recommends the most suitable ones based on your budget, location, and preferences.

## Features

- Scrapes rental listings from:
  - Apartments.com (via Selenium + BeautifulSoup)
  - Airbnb (via dynamic scraping)
  - Furnished Finder (via Apify API)
- Cleans and merges listings into a single dataset
- Intelligent filtering based on:
  - Price
  - Location
  - Amenities (WiFi, Gym, Washer, etc.)
- Match scoring for smarter ranking
- Streamlit web app for interactive user input and results
- Modular and easy-to-extend architecture



