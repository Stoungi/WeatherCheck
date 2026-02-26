import json

class WeatherReader:
    def __init__(self, raw_data):
        self.data = raw_data

    @staticmethod
    def build_url(config_path, system, city):
        with open(config_path, 'r') as f:
            config = json.load(f)

        # Pull the real key and the template
        api_key = config.get('api_key')
        template = config.get('urls', {}).get(system)

        if not api_key or api_key == "YOUR_KEY_FROM_VISUAL_CROSSING":
            raise ValueError("Error: You haven't replaced the placeholder key in config.json")

        # Inject the city and the key into the URL
        return template.format(location=city, key=api_key)

    def get_location(self):
        return self.data.get('resolvedAddress', 'Unknown')

    def get_current_conditions(self):
        return self.data.get('currentConditions', {})

    def get_forecast_days(self):
        return self.data.get('days', [])
