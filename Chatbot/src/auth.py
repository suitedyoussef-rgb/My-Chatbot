def Auth():
    
    print("\n1-sighn in")
    print("2-login")

    ch = input("\n")

    if ch == "1":
        while True:

            name = input("Username: ")
            passw = input("Password: ")

            with open("data/user.txt","a+") as file: # Use 'with' for proper file handling
                file.seek(0) # Go to the beginning of the file to read
                f = file.read()
                
                if f"\n{name},{passw}" in f or f"{name},{passw}" == f.strip(): # Check for exact match, including at start of file
                    print("Account already exists\n")
                else:
                    file.write(f"\n{name},{passw}")
                    print("Account created successfully!\n")
                    return name # Return name upon successful sign-up
            break # Break after successful sign-up or if account exists

    elif ch == "2": # Changed to elif for proper flow
        while True:
    
            name = input("Username: ")
            passw = input("Password: ")

            try:
                with open("data/user.txt","r") as file: 
                    f = file.read()
                    
                    if f"\n{name},{passw}" in f or f"{name},{passw}" == f.strip(): # Check for exact match
                        print("\nSuccessfully logged in\n\n")
                        return name # Return name upon successful login
                    
                    else:
                        print("Account doesn't exist or incorrect credentials\n")
                        continue # Continue asking for login if incorrect
            except FileNotFoundError:
                print("No accounts found. Please sign up first.\n")
                continue
 