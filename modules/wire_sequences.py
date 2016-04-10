def wire_sequences():
    occurrence = 1
    redwire = 0
    bluewire = 0
    blackwire = 0
    while occurrence <= 9:
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|                    WIRE SEQUENCES                     |")
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("| Sequence: " + str(occurrence) + "                                           |")
        print("+-------------------------------------------------------+")
        print("| Red Occurrences: " + str(redwire) + "                                    |")
        print("| Blue Occurrences: " + str(bluewire) + "                                   |")
        print("| Black Occurrences: " + str(blackwire) + "                                  |")
        print("+-------------------------------------------------------+")
        print('| Type "next" twice to move to the next sequence.       |')
        print('| Type "exit" twice to exit to the menu.                |')
        print("+-------------------------------------------------------+")
        colorwire = str(input("| Wire color: "))
        connectto = str(input("| Connected to: "))
        if colorwire == "red":
            redwire += 1
        elif colorwire == "blue":
            bluewire += 1
        elif colorwire == "black":
            blackwire += 1

        sequence = True
        while sequence == True:
            if colorwire == "red":
                if redwire == 1 and connectto == "c":
                    print("+=======================================================+")
                    print("| Cut the red wire.                                     |")
                    print("+=======================================================+")
                    sequence = False
                elif redwire == 2 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the red wire.                                     |")
                    print("+=======================================================+")
                    sequence = False
                elif redwire == 3 and connectto == "a":
                    print("+=======================================================+")
                    print("| Cut the red wire.                                     |")
                    print("+=======================================================+")
                    sequence = False
                elif redwire == 4:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the red wire.                                     |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the red wire.                                     |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the red wire.                               |")
                        print("+=======================================================+")
                        sequence = False
                elif redwire == 5 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the red wire.                                     |")
                    print("+=======================================================+")
                    sequence = False
                elif redwire == 6:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the red wire.                                     |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the red wire.                                     |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the red wire.                               |")
                        print("+=======================================================+")
                        sequence = False
                elif redwire == 7:
                    print("+=======================================================+")
                    print("| Cut the red wire.                                     |")
                    print("+=======================================================+")
                    sequence = False
                elif redwire == 8:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the red wire.                                     |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "b":
                        print("+=======================================================+")
                        print("| Cut the red wire.                                     |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the red wire.                               |")
                        print("+=======================================================+")
                        sequence = False
                elif redwire == 9 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the red wire.                                     |")
                    print("+=======================================================+")
                    sequence = False
                else:
                    print("+=======================================================+")
                    print("| Don't cut the red wire.                               |")
                    print("+=======================================================+")
                    sequence = False
            elif colorwire == "blue":
                if bluewire == 1 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the blue wire.                                    |")
                    print("+=======================================================+")
                    sequence = False
                elif bluewire == 2:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the blue wire.                                    |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the blue wire.                                    |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the blue wire.                              |")
                        print("+=======================================================+")
                        sequence = False
                elif bluewire == 3 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the blue wire.                                    |")
                    print("+=======================================================+")
                    sequence = False
                elif bluewire == 4 and connectto == "a":
                    print("+=======================================================+")
                    print("| Cut the blue wire.                                    |")
                    print("+=======================================================+")
                    sequence = False
                elif bluewire == 5 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the blue wire.                                    |")
                    print("+=======================================================+")
                    sequence = False
                elif bluewire == 6:
                    if connectto == "b":
                        print("+=======================================================+")
                        print("| Cut the blue wire.                                    |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the blue wire.                                    |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the blue wire.                              |")
                        print("+=======================================================+")
                        sequence = False
                elif bluewire == 7 and connectto == "c":
                    print("+=======================================================+")
                    print("| Cut the blue wire.                                    |")
                    print("+=======================================================+")
                    sequence = False
                elif bluewire == 8:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the blue wire.                                    |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the blue wire.                                    |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Cut the blue wire.                                    |")
                        print("+=======================================================+")
                        sequence = False
                elif bluewire == 9 and connectto == "a":
                    print("+=======================================================+")
                    print("| Cut the blue wire.                                    |")
                    print("+=======================================================+")
                    sequence = False
                else:
                    print("+=======================================================+")
                    print("| Don't cut the blue wire.                              |")
                    print("+=======================================================+")
                    sequence = False
            elif colorwire == "black":
                if blackwire == 1:
                    print("+=======================================================+")
                    print("| Cut the black wire.                                   |")
                    print("+=======================================================+")
                    sequence = False
                elif blackwire == 2:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the black wire.                             |")
                        print("+=======================================================+")
                        sequence = False
                elif blackwire == 3 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the black wire.                                   |")
                    print("+=======================================================+")
                    sequence = False
                elif blackwire == 4:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the black wire.                             |")
                        print("+=======================================================+")
                        sequence = False
                elif blackwire == 5 and connectto == "b":
                    print("+=======================================================+")
                    print("| Cut the black wire.                                   |")
                    print("+=======================================================+")
                    sequence = False
                elif blackwire == 6:
                    if connectto == "b":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the black wire.                             |")
                        print("+=======================================================+")
                        sequence = False
                elif blackwire == 7:
                    if connectto == "a":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    elif connectto == "c":
                        print("+=======================================================+")
                        print("| Cut the black wire.                                   |")
                        print("+=======================================================+")
                        sequence = False
                    else:
                        print("+=======================================================+")
                        print("| Don't cut the black wire.                             |")
                        print("+=======================================================+")
                        sequence = False
                elif blackwire == 8 and connectto == "c":
                    print("+=======================================================+")
                    print("| Cut the black wire.                                   |")
                    print("+=======================================================+")
                    sequence = False
                elif blackwire == 9 and connectto == "c":
                    print("+=======================================================+")
                    print("| Cut the black wire.                                   |")
                    print("+=======================================================+")
                    sequence = False
                else:
                    print("+=======================================================+")
                    print("| Don't cut the black wire.                             |")
                    print("+=======================================================+")
                    sequence = False
            if colorwire == "next" and connectto == "next":
                occurrence += 1
                print("+-------------------------------------------------------+\n| Next sequence")
                sequence = False
            elif colorwire == "exit" and connectto == "exit":
                occurrence = 10
                sequence = False
            else:
                sequence = False
