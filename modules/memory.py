from run import bomb_info


def memory():
    state = True
    while state == True:
        label = []
        positions = []
        print("==========================================")
        print("Memory Module Solver")
        print("==========================================")
        stageone = int(input('Stage One display: '))
        print("------------------------------------------")
        if stageone == 1:
            print("==========================================")
            print("Press the button in the second position.")
            print("==========================================")
            ansone = int(input("What is the label? "))
            print("------------------------------------------")
            positions.append(2)
            label.append(ansone)
        elif stageone == 2:
            print("==========================================")
            print("Press the button in the second position.")
            print("==========================================")
            anstwo = int(input("What is the label? "))
            print("------------------------------------------")
            positions.append(2)
            label.append(anstwo)
        elif stageone == 3:
            print("==========================================")
            print("Press the button in the third position.")
            print("==========================================")
            ansthree = int(input("What is the label? "))
            print("------------------------------------------")
            positions.append(3)
            label.append(ansthree)
        else:
            print("==========================================")
            print("Press the button in the fourth position.")
            print("==========================================")
            ansfour = int(input("What is the label? "))
            print("------------------------------------------")
            positions.append(4)
            label.append(ansfour)
        stagetwo = int(input('Stage Two display: '))
        print("------------------------------------------")
        if stagetwo == 1:
            print("==========================================")
            print('Press the button labeled "4".')
            print("==========================================")
            ansfive = int(input("What is the position? "))
            print("------------------------------------------")
            label.append(4)
            positions.append(ansfive)
        elif stagetwo == 2:
            print("==========================================")
            print('Press the button in position "' + str(positions[0]) + '".')
            print("==========================================")
            llabel = int(input("What is the label? "))
            print("------------------------------------------")
            poss = positions[0]
            positions.append(poss)
            label.append(llabel)
        elif stagetwo == 3:
            print("==========================================")
            print("Press the button in the first position.")
            print("==========================================")
            blah = int(input("What is the label? "))
            print("------------------------------------------")
            positions.append(1)
            label.append(blah)
        else:
            print("==========================================")
            print('Press the button in position "' + str(positions[0]) + '".')
            print("==========================================")
            labell = int(input("What is the label? "))
            print("------------------------------------------")
            poss = positions[0]
            positions.append(poss)
            label.append(labell)
        stagethree = int(input('Stage Three display: '))
        print("------------------------------------------")
        if stagethree == 1:
            if stagetwo == 1:
                print("==========================================")
                print('Press the button labeled "4".')
                print("==========================================")
                newans = int(input("What is the position? "))
                print("------------------------------------------")
                label.append(4)
                positions.append(newans)
            else:
                print("==========================================")
                print('Press the button labeled "' + str(label[1]) + '".')
                print("==========================================")
                ansseven = int(input("What is the position? "))
                print("------------------------------------------")
                lab = label[1]
                label.append(lab)
                positions.append(ansseven)
        elif stagethree == 2:
            print("==========================================")
            print('Press the button labeled "' + str(label[0]) + '".')
            print("==========================================")
            anseight = int(input("What is the position? "))
            print("------------------------------------------")
            lab = label[0]
            label.append(lab)
            positions.append(anseight)
        elif stagethree == 3:
            print("==========================================")
            print("Press the button in the third position.")
            print("==========================================")
            ansnine = int(input("What is the label? "))
            print("------------------------------------------")
            positions.append(3)
            label.append(ansnine)
        else:
            print("==========================================")
            print('Press the button labeled "4"')
            print("==========================================")
            ansten = int(input("What is the position? "))
            print("------------------------------------------")
            label.append(4)
            positions.append(ansten)
        stagefour = int(input('Stage Four display: '))
        print("------------------------------------------")
        if stagefour == 1:
            print("==========================================")
            print('Press the button in position "' + str(positions[0]) + '".')
            print("==========================================")
            anseleven = int(input("What is the label? "))
            print("------------------------------------------")
            poss = positions[0]
            positions.append(poss)
            label.append(anseleven)
        elif stagefour == 2:
            print("==========================================")
            print("Press the button in the first position.")
            print("==========================================")
            anstwelve = int(input("What is the label? "))
            print("------------------------------------------")
            positions.append(1)
            label.append(anstwelve)
        elif stagefour == 3:
            print("==========================================")
            print('Press the button in position "' + str(positions[1]) + '".')
            print("==========================================")
            ansthirteen = int(input("What is the label? "))
            print("------------------------------------------")
            poss = positions[1]
            positions.append(poss)
            label.append(ansthirteen)
        else:
            print("==========================================")
            print('Press the button in the "' + str(positions[1]) + '".')
            print("==========================================")
            ansfourteen = int(input("What is the label? "))
            print("------------------------------------------")
            poss = positions[1]
            positions.append(poss)
            label.append(ansfourteen)
        stagefive = int(input('Stage Five display: '))
        print("------------------------------------------")
        if stagefive == 1:
            print("==========================================")
            print("Press the button labeled " + str(label[0]))
            print("==========================================")
        elif stagefive == 2:
            print("==========================================")
            print("Press the button labeled " + str(label[1]))
            print("==========================================")
        elif stagefive == 3:
            print("==========================================")
            print("Press the button labeled " + str(label[3]))
            print("==========================================")
        else:
            print("==========================================")
            print("Press the button labeled " + str(label[2]))
            print("==========================================")
        done = input('Module solved. Type "done" to exit: ')
        if done == "done":
            state = False
        else:
            state = True