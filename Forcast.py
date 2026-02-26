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
        """Internal helper to ensure we have data before processing."""
        if self.reader is None:
            try:
                url = WeatherReader.build_url(self.config_path, self.system, self.city)
                response = requests.get(url)
                response.raise_for_status()
                self.reader = WeatherReader(response.json())
                return True
            except Exception as e:
                # We return a string error message if it fails
                return False
        return True

    def get_today(self) -> str:
        """Returns today's weather as a formatted string."""
        if not self._ensure_data_loaded():
            return "Error: Could not retrieve data."

        location = self.reader.get_location()
        current = self.reader.get_current_conditions()

        temp = current.get('temp', 'N/A')
        cond = current.get('conditions', 'Unknown')

        lines = [
            f"--- TODAY'S FORECAST: {location} ---",
            f"Conditions: {cond}",
            f"Temperature: {temp}{self.unit}",
            "-" * 40
        ]
        return "\n".join(lines)

    def get_week(self) -> str:
        """Returns the 7-day outlook as a formatted string."""
        if not self._ensure_data_loaded():
            return "Error: Could not retrieve data."

        days = self.reader.get_forecast_days()

        lines = ["--- WEEK'S FORECAST ---"]
        for day in days[1:8]:
            date = day.get('datetime')
            high = day.get('tempmax')
            low = day.get('tempmin')
            cond = day.get('conditions')
            lines.append(f"{date}: {cond:20} | High: {high}{self.unit} / Low: {low}{self.unit}")

        lines.append("-" * 40)
        return "\n".join(lines)


