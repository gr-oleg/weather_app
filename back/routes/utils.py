from urllib.parse import urlencode

from back.config import WEATHER_API_KEY


def build_weather_query(base_url: str, city: str, imperial=False) -> str:
    units = "imperial" if imperial else "metric"
    request_data = {'q': city,
                    'appid': WEATHER_API_KEY,
                    'units': units}
    url_values = urlencode(request_data)
    full_url = base_url + '?' + url_values
    return full_url
