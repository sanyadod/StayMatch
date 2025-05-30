import streamlit as st
from scripts.apartments_scraper import scrape_apartments
from scripts.airbnb_scraper import scrape_airbnb
from scripts.furnishedfinder_scraper import scrape_furnishedfinder
from scripts.recommender import recommend_listings

st.title("Temporary Housing Finder for Internships")

location = st.text_input("Enter the location (e.g., 'new-york-ny'):")
checkin = st.date_input("Check-in date")
checkout = st.date_input("Check-out date")
max_price = st.number_input("Maximum monthly rent", min_value=0)

if st.button("Find Apartments"):
    st.write("Scraping data, please wait...")
    apartments_df = scrape_apartments(location)
    airbnb_df = scrape_airbnb(location, checkin.strftime('%Y-%m-%d'), checkout.strftime('%Y-%m-%d'))
    # Replace 'YOUR_API_TOKEN' and 'START_URL' with actual values
    furnished_df = scrape_furnishedfinder('YOUR_API_TOKEN', 'START_URL')

    combined_df = pd.concat([apartments_df, airbnb_df, furnished_df], ignore_index=True)
    recommendations = recommend_listings(combined_df, max_price, location)
    st.write("Recommended Listings:")
    st.dataframe(recommendations)
