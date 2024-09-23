import pandas as pd
data = {
    'property ID': [1, 2, 3, 4, 5],
    'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb', 'City Center'],
    'number of bedrooms': [3, 5, 4, 6, 2],
    'area in square feet': [1500, 2500, 2000, 2800, 1200],
    'listing price': [500000, 750000, 600000, 850000, 400000]
}

property_data = pd.DataFrame(data)
average_price_by_location = property_data.groupby('location')['listing price'].mean()
print("\nAverage Listing Price by Location:")
print(average_price_by_location)
properties_more_than_four_bedrooms = property_data[property_data['number of bedrooms'] > 4]
count_properties = properties_more_than_four_bedrooms.shape[0]
print("\nNumber of Properties with More Than Four Bedrooms:")
print(count_properties)
property_with_largest_area = property_data.loc[property_data['area in square feet'].idxmax()]
print("\nProperty with the Largest Area:")
print(property_with_largest_area)
