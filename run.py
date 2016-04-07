from simple_wires import simple_wires
from complex_wires import complex_wires
from wire_sequences import wire_sequences
from button import button
from simon_says import simon_says
from whos_on_first import whos_on_first
from memory import memory
from morse_code import morse_code
from password import password

sernum = int(input("Last digit of the Serial Number: "))
servowel = input("Does the Serial Number contain a vowel? (yes/no): ")
battery = int(input("How many batteries?: "))
pport = input("Parallel Port? (yes/no): ")
car = input("Lit CAR indicator? (yes/no): ")
frk = input("Lir FRK indicator? (yes/no): ")
status = 1
while status == 1:
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
    module = int(input("What module would you like to solve?  "))
    if module == 1:
        simple_wires()
    elif module == 2:
        complex_wires()
    elif module == 3:
        wire_sequences()
    elif module == 4:
        button()
    elif module == 5:
        print("Symbols can't be solved without eyes.")
    elif module == 6:
        simon_says()
    elif module == 7:
        whos_on_first()
    elif module == 8:
        memory()
    elif module == 9:
        morse_code()
    elif module == 10:
        print("Maze can't be solved without eyes. Or good AI scripting ;)")
    elif module == 11:
        password()


def simple_wires():
    return simple_wires()


def complex_wires():
    return complex_wires()


def button():
    return button()


def simon_says():
    return simon_says()


def whos_on_first():
    return whos_on_first()


def memory():
    return memory()


def morse_code():
    return morse_code()


def password():
    return password()


