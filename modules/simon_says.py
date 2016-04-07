def simon_says(servowel):
    print("------------------------------------------")
    print("Simon Says Solver")
    print("------------------------------------------")
    if servowel == "yes":
        state = True
        while state == True:
            print("------------------------------------------")
            print('Type "69" to exit')
            print("------------------------------------------")
            strikes = int(input("How many Strikes? "))
            if strikes == 0:
                print("==========================================")
                print("| 0 Strikes |      Vowel     |")
                print("==========================================")
                print("| Red | Blue | Green | Yellow |")
                print("==========================================")
                print("| Blue | Red | Yellow | Green | <- Button to press")
            elif strikes == 1:
                print("==========================================")
                print("| 1 Strike |      Vowel     |")
                print("==========================================")
                print("| Red | Blue | Green | Yellow |")
                print("==========================================")
                print("| Yellow | Green | Blue | Red | <- Button to press")
            elif strikes == 2:
                print("==========================================")
                print("| 2 Strikes |      Vowel     |")
                print("==========================================")
                print("| Red | Blue | Green | Yellow |")
                print("==========================================")
                print("| Green | Red | Yellow | Blue | <- Button to press")
            elif strikes == 69:
                state = False
    elif servowel == "no":
        state = True
        while state == True:
            print("------------------------------------------")
            print('Type "69" to exit.')
            print("------------------------------------------")
            strikes = int(input("How many Strikes? "))
            if strikes == 0:
                print("==========================================")
                print("| 0 Strikes |    No Vowel     |")
                print("==========================================")
                print("| Red | Blue | Green | Yellow |")
                print("==========================================")
                print("| Blue | Yellow | Green | Red | <- Button to press")
            elif strikes == 1:
                print("==========================================")
                print("| 1 Strike |   No Vowel     |")
                print("==========================================")
                print("| Red | Blue | Green | Yellow |")
                print("==========================================")
                print("| Red | Blue | Yellow | Green | <- Button to press")
            elif strikes == 2:
                print("==========================================")
                print("| 2 Strikes |   No Vowel     |")
                print("==========================================")
                print("| Red | Blue | Green | Yellow |")
                print("==========================================")
                print("| Yellow | Green | Blue | Red | <- Button to press")
            elif strikes == 69:
                state = False
    else:
        print("I have no eyes. That was your fault.")
