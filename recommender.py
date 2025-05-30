import pandas as pd

def recommend_listings(df, max_price, preferred_location):
    df['numeric_price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    recommended = df[
        (df['numeric_price'] <= max_price) &
        (df['address'].str.contains(preferred_location, case=False))
    ]
    return recommended