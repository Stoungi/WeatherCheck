from Forcast import WeatherPresenter

# --- SETTINGS ---
target_city =  "Washington" #Options: whichever Location, use capital starting letter
target_system = "us" #Options: "metric" or "us"


# 1. Initialize the presenter
presenter = WeatherPresenter(target_city, target_system)

# 2. Use the specific methods directly
presenter.todays_forecast()
presenter.weeks_forecast()
