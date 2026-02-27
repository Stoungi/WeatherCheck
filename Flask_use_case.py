from flask import Flask, request
from Forcast import WeatherPresenter

app = Flask(__name__)

# Initialize the presenter
presenter = WeatherPresenter("Athens", "metric", "config.json")

@app.route('/weather')
def get_weather():
    # Use the new dictionary-based method
    # 1. Get today's weather (includes astronomy and current hour)
    # We pass 'hours': 3 to show the next few hours in the response
    today_data = presenter.get_forecast({"forecast": "today", "hours": 3})

    # 2. Get the weekly outlook
    week_data = presenter.get_forecast({"forecast": "week"})

    return f"{today_data}\n\n{week_data}"

@app.route('/weather/hourly')
def get_hourly_weather():
    """
    Optional: An endpoint that lets you specify hours via URL parameter
    Example: http://127.0.0.1:5000/weather/hourly?count=5
    """
    count = request.args.get('count', default=8, type=int)
    return presenter.get_forecast({"forecast": "today", "hours": count})

if __name__ == "__main__":
    app.run(port=5000)

# curl http://127.0.0.1:5000/weather
