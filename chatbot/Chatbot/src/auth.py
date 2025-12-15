def Auth():
    print("\n1-sighn in")
    print("2-login")

    ch = input("\n")

    if ch == "1":
        while True:

            name = input("Username: ")
            passw = input("Password: ")

            with open("data/user.txt","a+") as file:
                file.seek(0)
                f = file.read()
                
                if f"\n{name},{passw}" in f or f"{name},{passw}" == f.strip():
                    print("Account already exists\n")
                else:
                    file.write(f"\n{name},{passw}")
                    print("Account created successfully!\n")
                    return name

    elif ch == "2":
        while True:
    
            name = input("Username: ")
            passw = input("Password: ")

            try:
                with open("data/user.txt","r") as file: 
                    f = file.read()
                    
                    if f"\n{name},{passw}" in f or f"{name},{passw}" == f.strip():
                        print("\nSuccessfully logged in\n\n")
                        return name
                    
                    else:
                        print("Account doesn't exist or incorrect credentials\n")
                        continue
            except FileNotFoundError:
                print("No accounts found. Please sign up first.\n")
                continue