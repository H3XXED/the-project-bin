import requests
import json
from datetime import datetime
import plotly.express as px

# Define the USGS Earthquake API URL
api_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'

# Make the HTTP request to get the data
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    all_eq_data = response.json()

    # Examine all earthquakes in the dataset.
    all_eq_dicts = all_eq_data['features']

    mags, lons, lats, eq_titles, eq_dates = [], [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        eq_title = eq_dict['properties']['title']
        eq_date = eq_dict['properties']['time'] / 1000  # Convert epoch timestamp to seconds

        # Only include earthquakes with valid magnitude values
        if mag >= 0:
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
            eq_titles.append(eq_title)
            eq_dates.append(eq_date)

    # Convert epoch timestamps to readable date strings
    eq_dates = [datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S') for date in eq_dates]

    title = 'Global Earthquakes'
    fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags,
                         color_continuous_scale='inferno',
                         labels={'color': 'Magnitude'},
                         projection='natural earth', hover_name=eq_titles, hover_data={'Date': eq_dates})
    fig.show()
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")

