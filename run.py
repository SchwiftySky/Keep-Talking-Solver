from modules import simple_wires, complex_wires, wire_sequences, button, simon_says, \
    whos_on_first, memory, morse_code, password

status = 1
while status == 1:
    try:
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|                       BOMB INFO                       |")
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        sernum = int(input("| Last digit of the Serial Number: "))
        servowel = input("| Does the Serial Number contain a vowel? (yes/no): ")
        battery = int(input("| How many batteries: "))
        pport = input("| Parallel Port (yes/no): ")
        car = input("| Lit CAR indicator (yes/no): ")
        frk = input("| Lit FRK indicator (yes/no): ")
        status = 2
    except ValueError:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("| Oops! That wasn't a valid input. Try again... |")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")

while status == 2:
    try:
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|        KEEP TALKING AND NOBODY EXPLODES SOLVER        |")
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("| 1. Simple Wires   | 5. Symbols        | 9. Morse Code |")
        print("| 2. Complex Wires  | 6. Simon Says     | 10. Maze      |")
        print("| 3. Wire Sequences | 7. Who's on First | 11. Password  |")
        print("| 4. Button         | 8. Memory         |               |")
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("| Note: Numbers only                                    |")
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        module = int(input("| What module would you like to solve?  "))
        if module == 1:
            simple_wires.simple_wires(sernum)
        elif module == 2:
            complex_wires.complex_wires(battery, pport, sernum)
        elif module == 3:
            wire_sequences.wire_sequences()
        elif module == 4:
            button.button(battery, frk, car)
        elif module == 5:
            print("Symbols can't be solved without eyes.")
        elif module == 6:
            simon_says.simon_says(servowel)
        elif module == 7:
            whos_on_first.whos_on_first()
        elif module == 8:
            memory.memory()
        elif module == 9:
            morse_code.morse_code()
        elif module == 10:
            print("Maze can't be solved without eyes.")
        elif module == 11:
            password.password()
    except ValueError:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("| Oops! That wasn't a valid input. Try again... |")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
