import math
import requests
import numexpr as ne

def Matho():
    while True:
            try:
                # Show math options
                print("what do you want to calculate?")
                print("1-normal calculator-")
                print("2-smart calculator-")
                print("3-geometry-")
                print("4-temp calculator-")
                print("5-tip calculator-")
                print("6-currency converter")
                print("press X to go to the main menu")
                choice = input("")

                # --- Normal calculator (uses eval on the typed expression) ---
                if choice == "1":
                    expression = input("enter equation ")
                    if not expression.strip():
                        print("Please enter an expression.")
                        continue
                    print(ne.evaluate(expression))

                # --- Smart calculator shortcuts (sqrt, cbrt, tan, cosine) ---
                if choice == "2":
                    print("1-sqrt-")
                    print("2-cbrt- (cube root)")
                    print("3-tan-")
                    print("4-cosine-")
                    answer = input("Choose option 1-4: ")

                    # Typing 'stop' skips this sub-block and reprints the submenu
                    if answer == "stop":
                        continue

                    # sqrt
                    elif answer == "1":
                        num23 = float(input(""))
                        print(math.sqrt(num23))

                    # cbrt (note: math.cbrt exists in Python 3.11+)
                    elif answer == "2":
                        num11 = float(input(""))
                        try:
                            print(math.cbrt(num11))
                        except AttributeError:
                            # Fallback for older Python versions
                            print(num11**(1/3))

                    # tan
                    elif answer == "3":
                        num12 = float(input(""))
                        print(math.tan(num12))

                    # cosine
                    if answer == "4":
                        num = float(input(""))
                        print(math.cos(num))

                # --- Geometry calculators (area / perimeter / volume) ---
                if choice == "3":
                    print("area")
                    print("perimeter")
                    print("volume")
                    op = input("")

                    # ----- AREA -----
                    if op == "1":
                        print("1-square")
                        print("2-rectangle")
                        print("3-triangle")
                        print("4-paralellogram")
                        shape = input("choose shape ")

                        # square area
                        if shape == "1":
                            side = float(input("enter side "))
                            print(side**2)

                        # rectangle area
                        elif shape == "2":
                            length = float(input("enter the length "))
                            width = float(input("enter the width "))
                            print(length * width)

                        # triangle area
                        elif shape == "3":
                            base = float(input("enter base "))
                            height = float(input("enter height "))
                            print((1/2) * (base * height))

                        # parallelogram area
                        elif shape == "4":
                            base1 = float(input("enter base "))
                            hight = float(input("enter height "))
                            print(base1 * hight)

                        # go back to previous menu
                        elif shape == "stop":
                            continue
                        else:
                            print("this shape doesent exsist!")

                    # ----- PERIMETER -----
                    if op == "2":
                        print("1-square")
                        print("2-rectangle")
                        print("3-triangle")
                        print("4-paralellogram")
                        shape = input("choose shape ")

                        # square perimeter
                        if shape == "1":
                            side = float(input("enter side "))
                            print(side * 4)

                        # rectangle perimeter
                        elif shape == "2":
                            length = float(input("enter the length "))
                            width = float(input("enter the width "))
                            print(2 * (length + width))

                        # triangle perimeter
                        elif shape == "3":
                            side1 = float(input("enter first side "))
                            side2 = float(input("enter second side ")) 
                            side3 = float(input("enter third side "))
                            print(side1 + side2 + side3)

                        # parallelogram "perimeter" (here uses base + height as sides)
                        elif shape == "4":
                            base1 = float(input("enter base "))
                            side2 = float(input("enter second side (adjacent to base) ")) # Clarified input for parallelogram side
                            print(2 * (base1 + side2))

                        # go back to previous menu
                        elif shape == "stop":
                            continue
                        else:
                            print("this shape doesent exsist!")

                    # ----- VOLUME -----
                    if op == "3":
                        print("1-cuboid")
                        print("2-rectangular prism") # Removed underscore
                        shape = input("choose shape ")

                        # cube volume
                        if shape == "1":
                            side = float(input("enter side length ")) # Clarified input for cube
                            print(side**3)

                        # rectangular prism volume
                        elif shape == "2":
                            length = float(input("enter the length "))
                            width = float(input("enter the width "))
                            height = float(input("enter height "))
                            print(height * length * width)

                        # go back to previous menu
                        elif shape == "stop":
                            continue
                        else:
                            print("this shape doesent exsist!")

                # --- Temperature converter (C <-> F) ---
                if choice == "4":
                    unit = input("what is the unit that you want to convert to?{c or F?}")
                    if unit == "c":
                        num6 = float(input("enter temp "))
                        print((num6 - 32) * (5/9))

                    elif unit == "f":
                        num7 = float(input("enter temp "))
                        print(num7 * (9/5) + 32)

                # --- Tip calculator ---
                elif choice == "5":
                    num8 = float(input("enter total price "))
                    percent = float(input("enter tip percent "))
                    print(num8 * (percent/100) + num8)

                # --- Currency converter (uses open.er-api) ---
                elif choice == "6":
                    from_cur = input("from: ").upper()
                    to_cur = input("to: ").upper()
                    amount = float(input("amount: "))
                    try:
                        link = f"https://open.er-api.com/v6/latest/{from_cur}"
                        answer = requests.get(link)
                        answer.raise_for_status()
                        data = answer.json()
                        final = data["rates"][to_cur]      # get the exchange rate
                        final_answer = amount * final
                        print(f"{amount} {from_cur} is equal to {final_answer:.2f} {to_cur}")
                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching exchange rates: {e}")
                    except KeyError:
                        print(f"Invalid currency code provided. Could not find rates for '{from_cur}' or '{to_cur}'.")
                # --- Exit math submenu back to main menu ---
                elif choice.upper() == "X":
                    break

            # Basic math error handling
            except ZeroDivisionError:
                print("you cant divide by zero")

            except ValueError:
                print("Enter only numbers please ")
