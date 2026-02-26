import requests
from API_Reader import WeatherReader

class WeatherPresenter:
    def __init__(self, city, system, config_path="config.json"):
        self.city = city
        self.system = system
        self.config_path = config_path
        self.unit = "°C" if system == "metric" else "°F"
        self.reader = None

    def _ensure_data_loaded(self):
        """Internal helper to ensure we have data before displaying."""
        if self.reader is None:
            try:
                url = WeatherReader.build_url(self.config_path, self.system, self.city)
                response = requests.get(url)
                response.raise_for_status()
                self.reader = WeatherReader(response.json())
                return True
            except Exception as e:
                print(f"Error: Could not retrieve weather data. {e}")
                return False
        return True

    def todays_forecast(self):
        """Displays current weather details."""
        if not self._ensure_data_loaded():
            return

        location = self.reader.get_location()
        current = self.reader.get_current_conditions()

        temp = current.get('temp', 'N/A')
        cond = current.get('conditions', 'Unknown')

        print(f"\n--- TODAY'S FORECAST: {location} ---")
        print(f"Conditions: {cond}")
        print(f"Temperature: {temp}{self.unit}")
        print("-" * 40)

    def weeks_forecast(self):
        """Displays the 7-day outlook."""
        if not self._ensure_data_loaded():
            return
        location = self.reader.get_location()
        days = self.reader.get_forecast_days()

        print(f"--- WEEK'S FORECAST: {location} ---")
        for day in days[1:8]:
            date = day.get('datetime')
            high = day.get('tempmax')
            low = day.get('tempmin')
            cond = day.get('conditions')
            print(f"{date}: {cond:20} | High: {high}{self.unit} / Low: {low}{self.unit}")
        print("-" * 40)
