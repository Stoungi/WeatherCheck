import json

class WeatherReader:
    """Processes the JSON from Visual Crossing and stores it for easy access."""

    def __init__(self, raw_json):
        # Handle both string input and pre-parsed dictionaries
        if isinstance(raw_json, str):
            self.data = json.loads(raw_json)
        else:
            self.data = raw_json

    def get_current_conditions(self):
        return self.data.get('currentConditions', {})

    def get_forecast_days(self):
        return self.data.get('days', [])

    def get_location(self):
        return self.data.get('resolvedAddress', 'Unknown Location')
