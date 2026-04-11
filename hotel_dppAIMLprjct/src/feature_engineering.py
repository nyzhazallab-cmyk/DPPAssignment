import pandas as pd

def add_features(df):
    df['total_nights'] = df['stays_in_week_nights'] + df['stays_in_weekend_nights']
    df['total_people'] = df['adults'] + df['children'] + df['babies']

    df['price_per_person'] = df['adr'] / (df['total_people'] + 1)
    df['family_flag'] = (df['children'] + df['babies'] > 0).astype(int)

    return df