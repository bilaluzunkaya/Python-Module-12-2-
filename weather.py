import requests


API_KEY = "90e5f7a2117801f2db941acab81b46e2"


def get_coordinates(city_name):
    url = "http://api.openweathermap.org/geo/1.0/direct"

    params = {
        "q": city_name,
        "limit": 1,
        "appid": API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if not data:
        return None

    lat = data[0]["lat"]
    lon = data[0]["lon"]
    name = data[0]["name"]
    country = data[0]["country"]

    return lat, lon, name, country


def get_weather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"   
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    return description, temperature


def main():
    city_name = input("Enter the name of a municipality: ")

    try:
        location = get_coordinates(city_name)

        if location is None:
            print("Municipality not found.")
            return

        lat, lon, name, country = location

        description, temperature = get_weather(lat, lon)

        print(f"\nWeather in {name}, {country}:")
        print(f"Condition: {description}")
        print(f"Temperature: {temperature:.1f} °C")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching weather data: {e}")
    except KeyError:
        print("Unexpected API response.")


if __name__ == "__main__":
    main()
