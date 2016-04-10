def simple_wires(sernum):
    state = 1
    while state == 1:
        try:
            print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
            print("|                      SIMPLE WIRES                     |")
            print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
            print('| Type "0" to go to the main menu.                      |')
            print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
            wirecount = int(input("| How many wires? "))

            if wirecount == 3:
                print("+-------------------------------------------------------+")
                print("| List 3 wires separated by commas e.g. red,white,blue. |")
                print('| Type "0" to go to the main menu.                      |')
                print("+-------------------------------------------------------+")
                wirecolor = str(input("| Enter the wire colors: "))
                colorbreak = wirecolor.split(",")
                if "red" not in colorbreak:
                    print("+=======================================================+")
                    print("| Cut the second wire.                                  |")
                    print("+=======================================================+")
                elif colorbreak[-1] == "white":
                    print("+=======================================================+")
                    print("| Cut the last wire.                                    |")
                    print("+=======================================================+")
                elif colorbreak.count("blue") > 1:
                    print("+=======================================================+")
                    print("| Cut the last blue wire.                               |")
                    print("+=======================================================+")
                elif wirecolor == 0:
                    state = 0
                else:
                    print("+=======================================================+")
                    print("| Cut the last wire.                                    |")
                    print("+=======================================================+")
            elif wirecount == 4:
                print("+-------------------------------------------------------+")
                print("| List 4 wires separated by commas e.g. red,white,blue, |")
                print('| black. Type "0" to go to the main menu.               |')
                print("+-------------------------------------------------------+")
                wirecolor = str(input("| Enter the wire colors: "))
                colorbreak = wirecolor.split(",")
                if colorbreak.count("red") > 1 and sernum % 2 != 0:
                    print("+=======================================================+")
                    print("| Cut the last red wire.                                |")
                    print("+=======================================================+")
                elif colorbreak[-1] == "yellow" and colorbreak.count("red") == 0:
                    print("+=======================================================+")
                    print("| Cut the first wire.                                   |")
                    print("+=======================================================+")
                elif colorbreak.count("blue") == 1:
                    print("+=======================================================+")
                    print("| Cut the first wire.                                   |")
                    print("+=======================================================+")
                elif colorbreak.count("yellow") > 1:
                    print("+=======================================================+")
                    print("| Cut the last wire.                                    |")
                    print("+=======================================================+")
                elif wirecolor == 0:
                    state = 0
                else:
                    print("+=======================================================+")
                    print("| Cut the second wire.                                  |")
                    print("+=======================================================+")
            elif wirecount == 5:
                print("+-------------------------------------------------------+")
                print("| List 5 wires separated by commas e.g. red,white,blue, |")
                print('| black,yellow. Type "0" to go to the main menu.        |')
                print("+-------------------------------------------------------+")
                wirecolor = str(input("| Enter the wire colors: "))
                colorbreak = wirecolor.split(",")
                if colorbreak[-1] == "black" and sernum % 2 != 0:
                    print("+=======================================================+")
                    print("| Cut the fourth wire.                                  |")
                    print("+=======================================================+")
                elif colorbreak.count("red") and colorbreak.count("yellow") > 1:
                    print("+=======================================================+")
                    print("| Cut the first wire.                                   |")
                    print("+=======================================================+")
                elif colorbreak.count("black") == 0:
                    print("+=======================================================+")
                    print("| Cut the second wire.                                  |")
                    print("+=======================================================+")
                elif wirecolor == 0:
                    state = 0
                else:
                    print("+=======================================================+")
                    print("| Cut the first wire.                                   |")
                    print("+=======================================================+")
            elif wirecount == 6:
                print("+-------------------------------------------------------+")
                print("| List 6 wires separated by commas e.g. red,white,blue, |")
                print('| black,yellow,red. Type "0" to go to the main menu. |')
                print("+-------------------------------------------------------+")
                wirecolor = str(input("Enter the wire colors: "))
                colorbreak = wirecolor.split(",")
                if colorbreak.count("yellow") == 0 and sernum % 2 != 0:
                    print("+=======================================================+")
                    print("| Cut the third wire.                                   |")
                    print("+=======================================================+")
                elif colorbreak.count("yellow") == 1 and colorbreak.count("white") > 1:
                    print("+=======================================================+")
                    print("| Cut the fourth wire.                                  |")
                    print("+=======================================================+")
                elif colorbreak.count("red") == 0:
                    print("+=======================================================+")
                    print("| Cut the last wire.                                    |")
                    print("+=======================================================+")
                elif wirecolor == "0":
                    state = 0
                else:
                    print("+=======================================================+")
                    print("| Cut the fourth wire.                                  |")
                    print("+=======================================================+")
            elif wirecount == 0:
                state = 0
            else:
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("| Failed to find a wire count.                          |")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        except ValueError:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("| Oops! That wasn't a valid input. Try again...         |")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
