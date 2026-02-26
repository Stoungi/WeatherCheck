import json
import requests
import os

# Your class imports
from API_Reader import WeatherReader
from Forcast import WeatherPresenter

# --- CONFIGURATION ---
# Change these two variables to switch setups
target_system = "us"  # Options: "metric" or "us"
target_city = "Washington" #Options: whichever Location, use capital starting letter
# ---------------------

# 1. Load the JSON config file
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Error: config.json not found.")
    exit()

# 2. Extract the template and key
api_key = config.get('api_key')
url_template = config.get('urls', {}).get(target_system)

if not api_key or not url_template:
    print(f"Error: Missing info in config.json for '{target_system}'")
    exit()

# 3. Format the URL
# This replaces {location} and {key} inside the JSON's URL string
final_url = url_template.format(location=target_city, key=api_key)

# 4. Fetch and Display
try:
    print(f"Loading {target_system} weather for {target_city}...")
    response = requests.get(final_url)
    response.raise_for_status()

    # Process with your classes
    reader = WeatherReader(response.json())
    presenter = WeatherPresenter(reader)

    presenter.display_current_summary()
    presenter.display_weekly_forecast()

except Exception as e:
    print(f"An error occurred: {e}")
