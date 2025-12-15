
from auth import Auth
from ai import AI_Chatbot, image_generator
from general import general
from education import educate
from entertainment import entertain
from islamic_mode import Islamic
from weather import weather
from main_menu import main_menu as Main_menu
from mathematics import Matho

print("\n\nWelcome to the Chatbot Portal\n")

name = Auth()

while True:
    choice1 = Main_menu(name)

    if choice1 == "1":
        ch2 = input("\n1-AI chat\n2-AI Image Generator\n\n--->")

        if ch2 == "1":
            AI_Chatbot()

        elif ch2 == "2":
            image_generator()

        elif not ch2:
            print("\n")
            continue    

    elif choice1 == "2":
        weather()

    elif choice1 == "3":
        Islamic(name)

    elif choice1 == "4":
        entertain(name)

    elif choice1 == "5":
        educate(name)

    elif choice1 == "6":
        general(name)

    elif choice1 == "7":
        Matho()

    elif choice1.lower() == "x":
        print("Logging out...")
        break

    else:
        print("Invalid option, please try again.")