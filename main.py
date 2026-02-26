from Forcast import WeatherPresenter


# --- SETTINGS ---
target_city =  "Washington" #Options: whichever Location, use capital starting letter
target_system = "us" #Options: "metric" or "us"


# 1. Initialize the presenter
presenter = WeatherPresenter(target_city, target_system)

# 2. use the new methods for a more versatile usecase (like making a UI app or curl request)
print(presenter.get_today())
print(presenter.get_week())
