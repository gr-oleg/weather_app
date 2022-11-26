from backend.routes.weather.current import get_weather_info


result = get_weather_info(city="Lviv")
print(result)
