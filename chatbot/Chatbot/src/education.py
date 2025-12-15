def educate(name):
    import requests # Added import for requests
    print(f"Welcome {name} to Education mode") # Fixed f-string syntax
    print("")
    while True:

        print("1-Dictionary")
        print("2-Country Information")
        print("3-Astronomy facts")
        print("press x to exit")

        option = input("")

        if option == "1":
            word = input("Enter word or x to go back to main menu: ")

            if word.lower() == "x":
                    break
            try:
                url1 = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

                response = requests.get(url1)

                if response.status_code != 200:
                    print("Could not find the definition. Please check the word.")
                    continue

                data = response.json()

                meaning = data[0]["meanings"][0]["definitions"][0]["definition"]

                print("The word ",word," means:")
                print (meaning)   

                answer = input("continue?")

                if answer.lower() == "no":
                    break

                if answer.lower() == "yes":
                    continue
            except (requests.exceptions.RequestException, KeyError, IndexError):
                print("Could not find the definition. Please check the word or try again later.")
                continue

    #----------------------------------------------------------------------------------------------- 
        if option == "2":

            while True:

                country = input("Enter Country or x to exit: ")

                if country.lower() == "x":
                    break
                try:
                    url = f"https://restcountries.com/v3.1/name/{country}"

                    response = requests.get(url)

                    if response.status_code !=200:
                        print("country not found.Try again!")
                        continue


                    data = response.json()[0]

                    population = data["population"]
                    area = data["area"]
                    flag = data["flags"]["png"]
                    capital = data["capital"]

                    print("Giving Info for ",country,":")
                    print("")
                    print("Capital:",capital)
                    print("Population:",population)
                    print("Area:",area)
                    print("Flag image",flag)
                except (requests.exceptions.RequestException, KeyError, IndexError):
                    print("Could not retrieve country information. Please check the country name or try again later.")
                    continue

#---------------------------------------------------------------------------------           
        if option.lower() == "x":
            break             
   #-------------------------------------------------------------------------------------

        if option == "3":
            while True:
                try:
                    url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

                    response = requests.get(url)
                    response.raise_for_status()

                    data = response.json()

                    title = data["title"]
                    exp = data["explanation"]
                    url1 = data["url"]
                    date = data["date"]

                    print("Title:",title)
                    print("")
                    print("This image shows: ",exp)
                    print("")
                    print("Image:",url1)
                    print("")
                    print("Date:",date)
                    print("")
                    print('Continue?')

                    answer = input("")

                    if answer.lower() == "no":
                        break
                        
                    if answer.lower() == "yes":
                        continue
                except (requests.exceptions.RequestException, KeyError, IndexError):
                    print("Could not retrieve the astronomy fact. Please try again later.")
                    break
