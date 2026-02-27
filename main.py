from Forcast import WeatherPresenter

presenter = WeatherPresenter("Washington", "us")

# 1. Standard Today (This hour + Astronomy)
print(presenter.get_forecast({"forecast": "today"}))

# 2. Today + Next 4 hours
print(presenter.get_forecast({"forecast": "today", "hours": 4}))

# 3. Week's forecast
print(presenter.get_forecast({"forecast": "week"}))
