from flask import Flask
from Forcast import WeatherPresenter

app = Flask(__name__)


presenter = WeatherPresenter("Athens", "metric", "config.json")

@app.route('/weather')
def get_weather():

    return f"{presenter.get_today()}\n{presenter.get_week()}"

if __name__ == "__main__":

    app.run(port=5000)

# curl http://127.0.0.1:5000/weather
