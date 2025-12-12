
from auth import Auth
from ai import ai
from general import general
from education import educate
from entertainment import entertain
from islamic_mode import Islamic
from weather import Weather
from main_menu import Main_menu
from mathematics import Matho

def main():
    """Main function to run thbe chatbot portal."""
    print("\n\nWelcome to the Chatbot Portal")
    name = Auth()

    if not name:
        print("Authentication failed. Exiting.")
        return

    while True:
        choice1 = Main_menu(name)

        if choice1 == "1":
            ai()

        elif choice1 == "2":
            Weather()

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

if __name__ == "__main__":
    main()