def simon_says(servowel):
    print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    print("|                       SIMON SAYS                      |")
    print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
    if servowel == "yes":
        state = True
        while state == True:
            print("+-------------------------------------------------------+")
            print('| Type "69" to exit                                     |')
            print("+-------------------------------------------------------+")
            strikes = int(input("How many Strikes? "))
            if strikes == 0:
                print("+=======================================================+")
                print("| Vowel |                  0 Strikes                    |")
                print("+=======================================================+")
                print("| Flash |    Red    |   Blue   |   Green   |   Yellow   |")
                print("+-------+-----------+----------+-----------+------------+")
                print("| Press |    Blue   |   Red    |   Yellow  |   Green    |")
            elif strikes == 1:
                print("+=======================================================+")
                print("| Vowel |                  1 Strike                     |")
                print("+=======================================================+")
                print("| Flash |    Red    |   Blue   |   Green   |   Yellow   |")
                print("+-------+-----------+----------+-----------+------------+")
                print("| Press |   Yellow  |   Green  |   Blue    |    Red     |")
            elif strikes == 2:
                print("+=======================================================+")
                print("| Vowel |                  2 Strikes                    |")
                print("+=======================================================+")
                print("| Flash |    Red    |   Blue   |   Green   |   Yellow   |")
                print("+-------+-----------+----------+-----------+------------+")
                print("| Press |   Green   |   Red    |   Yellow  |    Blue    |")
            elif strikes == 69:
                state = False
    elif servowel == "no":
        state = True
        while state == True:
            print("+-------------------------------------------------------+")
            print('| Type "69" to exit.                                    |')
            print("+-------------------------------------------------------+")
            strikes = int(input("How many Strikes? "))
            if strikes == 0:
                print("+=======================================================+")
                print("| No Vowel |                0 Strikes                   |")
                print("+=======================================================+")
                print("| Flash |    Red    |   Blue   |   Green   |   Yellow   |")
                print("+-------+-----------+----------+-----------+------------+")
                print("| Press |    Blue   |  Yellow  |   Green   |    Red     |")
            elif strikes == 1:
                print("+=======================================================+")
                print("| No Vowel |                1 Strike                    |")
                print("+=======================================================+")
                print("| Flash |    Red    |   Blue   |   Green   |   Yellow   |")
                print("+-------+-----------+----------+-----------+------------+")
                print("| Press |    Red    |   Blue   |   Yellow  |   Green    |")
            elif strikes == 2:
                print("+=======================================================+")
                print("| No Vowel |                2 Strikes                   |")
                print("+=======================================================+")
                print("| Flash |    Red    |   Blue   |   Green   |   Yellow   |")
                print("+-------+-----------+----------+-----------+------------+")
                print("| Press |  Yellow   |   Green  |   Blue    |    Red     |")
            elif strikes == 69:
                state = False
