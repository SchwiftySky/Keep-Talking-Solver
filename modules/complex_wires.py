from run import battery, pport, sernum


def complex_wires():
    print("------------------------------------------")
    print("Complex Wires Solver")
    print("------------------------------------------")
    print("LED: on/off | Star: yes/no | Wire Color: red,red")
    print("------------------------------------------")
    state = 0
    while state <= 6:
        led = input("LED: ")
        wirecolor = input("Wire Color: ")
        star = input("Star: ")
        if star == "yes" and led == "off":
            print("==========================================")
            print("Cut the wire")
            print("==========================================")
            state += 1
        elif star == "yes" and wirecolor == "red":
            print("==========================================")
            print("Cut the wire")
            print("==========================================")
            state += 1
        elif star == "yes" and led == "on":
            if battery >= 2:
                print("==========================================")
                print("Cut the wire")
                print("==========================================")
                state += 1
            elif wirecolor == "red" and battery >= 2:
                print("==========================================")
                print("Cut the wire")
                print("==========================================")
                state += 1
            if wirecolor == "blue" and led == "on":
                if pport == "yes":
                    print("==========================================")
                    print("Cut the wire")
                    print("==========================================")
                    state += 1
            elif wirecolor == "blue":
                print("==========================================")
                print("Don't cut the wire")
                print("==========================================")
                state += 1
            elif wirecolor == "blue,red" or wirecolor == "red,blue":
                print("==========================================")
                print("Don't cut the wire")
                print("==========================================")
                state += 1
                if pport == "yes" and led == "off":
                    print("==========================================")
                    print("Cut the wire")
                    print("==========================================")
                    state += 1
                elif sernum % 2 == 0 and led == "on":
                    print("==========================================")
                    print("Cut the wire")
                    print("==========================================")
                    state += 1
                elif sernum % 2 == 0 and led == "off":
                    print("==========================================")
                    print("Cut the wire")
                    print("==========================================")
                    state += 1
        elif led == "on" and wirecolor == "red":
            if battery >= 2:
                print("==========================================")
                print("Cut the wire")
                print("==========================================")
                state += 1
        elif led == "on" and star == "no":
            print("==========================================")
            print("Don't cut the wire")
            print("==========================================")
            state += 1
        elif led == "on" and wirecolor == "blue":
            if pport == "yes":
                print("==========================================")
                print("Cut the wire")
                print("==========================================")
                state += 1
            else:
                print("==========================================")
                print("Don't cut the wire")
                print("==========================================")
                state += 1
        elif wirecolor == "blue" and sernum % 2 == 0:
                print("==========================================")
                print("Cut the wire")
                print("==========================================")
                state += 1
        elif wirecolor == "red" and sernum % 2 == 0:
            print("==========================================")
            print("Cut the wire")
            print("==========================================")
            state += 1
        elif led == "off" and star == "no":
            print("==========================================")
            print("Cut the wire")
            print("==========================================")
            state += 1
        else:
            print("==========================================")
            print("Don't cut the wire")
            print("==========================================")
            state += 1
