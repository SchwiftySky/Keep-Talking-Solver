def button(battery, frk, car):
    state = True
    while state == True:
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|                         BUTTON                        |")
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        try:
            buttcolor = str(input("Button color: "))
            butttext = str(input("Button text: "))
            if buttcolor == "blue" and butttext == "abort":
                print("+=======================================================+")
                print("| Hold the button. Release when the timer has a...      |")
                print("| Blue: 4, White: 1, Yellow: 5, Other: 1                |")
                print("+=======================================================+")
                state = False
            elif battery >= 2 and butttext == "detonate":
                print("+=======================================================+")
                print("| Press and immediately release the button.             |")
                print("+=======================================================+")
                state = False
            elif buttcolor == "white" and car == "yes":
                print("+=======================================================+")
                print("| Hold the button. Release when the timer has a...      |")
                print("| Blue: 4, White: 1, Yellow: 5, Other: 1                |")
                print("+=======================================================+")
                state = False
            elif battery >= 3 and frk == "yes":
                print("+=======================================================+")
                print("| Press and immediately release the button.             |")
                print("+=======================================================+")
                state = False
            elif buttcolor == "yellow":
                print("+=======================================================+")
                print("| Hold the button. Release when the timer has a...      |")
                print("| Blue: 4, White: 1, Yellow: 5, Other: 1                |")
                print("+=======================================================+")
                state = False
            elif buttcolor == "red" and butttext == "hold":
                print("+=======================================================+")
                print("| Press and immediately release the button.             |")
                print("+=======================================================+")
                state = False
            else:
                print("+=======================================================+")
                print("| Hold the button. Release when the timer has a...      |")
                print("| Blue: 4, White: 1, Yellow: 5, Other: 1                |")
                print("+=======================================================+")
                state = False
        except ValueError:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("| Oops! That wasn't a valid input. Try again...         |")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

