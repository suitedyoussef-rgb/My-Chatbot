def Islamic(name):    
    from datetime import datetime # Added import for datetime
    import requests # Added import for requests

    while True:
                print(f"Welcome {name} to Islamic mode") # Fixed f-string syntax
                print("1-When is Ramadan?")
                print("2-When is Eid Al-Fitr?")
                print("3-When is Eid Al-Adha?")
                print("4-Prayer Times")
                print("press X to go back to the main menu")
                print("")
                print("")
                
                command=input("")
                
                if command == "1":
                    current = datetime.now()
                    ramadan = datetime(2025, 3, 1)
                    difference = ramadan-current
                    print("Time left untill Ramadan is: ",difference," days")

                if command == "2":
                    current = datetime.now()
                    eid_f = datetime (2025,3,31)
                    difference = eid_f-current
                    print("Time left untill Eid Al-Fitr is: ",difference," days")

                if command == "3":
                    current = datetime.now()
                    eid_adha = datetime (2025,6,6)
                    difference = eid_adha-current
                    print("Time left untill Eid Al-Adha is: ",difference," days")

                
                if command == "4":
                    while True:
                        country=input("Enter country or X to exit: ")
                        if country.upper() == "X":
                            break
                        
                        city=input("Enter city or X to exit: ")
                        if city.upper() == "X":
                            break
                        
                        try:
                            pray_url = "https://api.aladhan.com/v1/timingsByCity"
                        
                            method=5
                            
                            params={"city":city,
                                    "country":country,
                                    "method":method}
                            
                            response=requests.get(pray_url,params=params)
                            response.raise_for_status() # Raise an exception for bad status codes
                            
                            data=response.json()
                            
                            # Check if the API returned data successfully
                            if data.get("code") == 200:
                                times=data["data"]["timings"]
                                
                                print("---Prayer Times in ",city," are:")
                                print("Fajr----->",times["Fajr"])
                                print("Sunrise----->",times["Sunrise"])
                                print("Duhr----->",times["Dhuhr"])
                                print("Asr----->",times["Asr"])
                                print("Maghrib----->",times["Maghrib"])
                                print("Ishaa----->",times["Isha"])
                            else:
                                print("Could not find prayer times for the specified location. Please check the city and country.")
                        
                        except (requests.exceptions.RequestException, KeyError):
                            print("Could not retrieve prayer times. Please check your connection or try again later.")
                            continue
                    
                if command.lower() == "x": # Corrected indentation for exit from Islamic mode
                    break    
