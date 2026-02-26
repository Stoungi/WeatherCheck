class WeatherPresenter:
    """Utilizes the WeatherReader to display formatted weather information."""

    def __init__(self, reader: WeatherReader, system: str):
        self.reader = reader
        self.system = system  # This will be "metric" or "us" from main.py

    def display_current_summary(self):
        location = self.reader.get_location()
        current = self.reader.get_current_conditions()

        temp = current.get('temp', 'N/A')
        conditions = current.get('conditions', 'Unknown')

        # Simple switch based on the input from main
        unit = "°C" if self.system == "metric" else "°F"

        print(f"--- Weather for {location} ---")
        print(f"Current Status: {conditions}")
        print(f"Temperature: {temp}{unit}")
        print("-" * 30)

    def display_weekly_forecast(self):
        days = self.reader.get_forecast_days()
        unit = "°C" if self.system == "metric" else "°F"

        print("Upcoming Forecast:")
        for day in days[:7]:
            date = day.get('datetime')
            high = day.get('tempmax')
            low = day.get('tempmin')
            cond = day.get('conditions')
            print(f"{date}: {cond} | High: {high}{unit} / Low: {low}{unit}")
