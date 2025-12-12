def Weather():
    import requests # Added import for requests
    while True:
        # Get city, then use Open-Meteo geocoding + forecast to fetch current temperature
        city = input("enter city or X to stop: ")
        
        if city.upper() == "x":
            break

        try:
            geo = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=" + city).json()
            
            if not geo or "results" not in geo or not geo["results"]:
                print("City not found. Please try again.")
                continue

            lat = geo["results"][0]["latitude"]
            lon = geo["results"][0]["longitude"]
            weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m").json()
            print(f"temperature in {city} is: {weather['current']['temperature_2m']} °C")
        except (requests.exceptions.RequestException, KeyError, IndexError) as e:
            print(f"An error occurred while fetching weather data: {e}. Please try again.")
        