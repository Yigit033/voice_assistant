import requests

def get_weather(city):
    api_key = "4286bf664230f420a343cdfa07541d16"  # OpenWeatherMap API anahtarınızı buraya ekleyin
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['weather'][0]['description'], data['current']['temp']
    else:
        return None
