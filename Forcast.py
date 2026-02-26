class WeatherPresenter:
    """Utilizes the WeatherReader to display formatted weather information."""

    def __init__(self, reader: WeatherReader):
        self.reader = reader

    def display_current_summary(self):
        location = self.reader.get_location()
        current = self.reader.get_current_conditions()

        temp = current.get('temp', 'N/A')
        conditions = current.get('conditions', 'Unknown')

        print(f"--- Weather for {location} ---")
        print(f"Current Status: {conditions}")
        print(f"Temperature: {temp}°F")
        print("-" * 30)

    def display_weekly_forecast(self):
        days = self.reader.get_forecast_days()
        print("Upcoming Forecast:")
        for day in days[:7]:
            date = day.get('datetime')
            high = day.get('tempmax')
            low = day.get('tempmin')
            cond = day.get('conditions')
            print(f"{date}: {cond} | High: {high}° / Low: {low}°")
