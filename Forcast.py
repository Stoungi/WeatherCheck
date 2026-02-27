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
        if self.reader is None:
            try:
                url = WeatherReader.build_url(self.config_path, self.system, self.city)
                response = requests.get(url)
                response.raise_for_status()
                self.reader = WeatherReader(response.json())
                return True
            except Exception:
                return False
        return True

    def _interpret_moon(self, phase):
        """Translates moon phase decimal to a description."""
        if phase == 0: return "New Moon"
        if phase == 0.5: return "Full Moon"
        if 0 < phase < 0.25: return "Waxing Crescent"
        if 0.25 <= phase < 0.5: return "Waxing Gibbous"
        if 0.5 < phase <= 0.75: return "Waning Gibbous"
        return "Waning Crescent"

    def get_forecast(self, request_dict: dict) -> str:
        if not self._ensure_data_loaded():
            return "Error: Could not retrieve data."

        scope = request_dict.get("forecast")
        location = self.reader.get_location()

        if scope == "today":
            current = self.reader.get_current_conditions()
            astro = self.reader.get_astronomy_today()

            lines = [
                f"--- TODAY'S WEATHER: {location} ---",
                f"Current Time: {current.get('datetime')}",
                f"Conditions: {current.get('conditions')}",
                f"Temperature: {current.get('temp')}{self.unit}",
                f"Sunrise: {astro.get('sunrise')} | Sunset: {astro.get('sunset')}",
                f"Moon Phase: {self._interpret_moon(astro.get('moonphase'))}"
            ]

            # If optional "hours" is provided, append the next X hours
            hour_count = request_dict.get("hours")
            if hour_count:
                lines.append(f"\n--- NEXT {hour_count} HOURS ---")
                hourly_data = self.reader.get_hourly_forecast()
                # Find current hour index to start forecast from now
                current_hour_str = current.get('datetime', '00:00:00')[:2]
                start_idx = int(current_hour_str)

                for h in hourly_data[start_idx + 1 : start_idx + 1 + int(hour_count)]:
                    lines.append(f"{h.get('datetime')[:5]}: {h.get('temp')}{self.unit} - {h.get('conditions')}")

            lines.append("-" * 40)
            return "\n".join(lines)

        elif scope == "week":
            days = self.reader.get_forecast_days()
            lines = [f"--- WEEK'S FORECAST: {location} ---"]
            for day in days[1:8]:
                lines.append(f"{day.get('datetime')}: {day.get('conditions'):20} | High: {day.get('tempmax')}{self.unit} / Low: {day.get('tempmin')}{self.unit}")
            lines.append("-" * 40)
            return "\n".join(lines)

        return "Error: Invalid forecast type."
