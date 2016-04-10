def whos_on_first():
    state = 1
    while state <= 5:
        tr = "| Top Right                                             |"
        mr = "| Middle Right                                          |"
        br = "| Bottom Right                                          |"
        tl = "| Top Left                                              |"
        ml = "| Middle Left                                           |"
        bl = "| Bottom Left                                           |"
        rdy = "| Yes, Okay, What, Middle, Left, Press, Right,          |" \
              "\n| Blank, Ready, No, First, Uhhh, Nothing, Wait          |"
        frst = "| Left, Okay, Yes, Middle, No, Right, Nothing,          |" \
               "\n| Uhhh, Wait, Ready, Blank, What, Press, First          |"
        no = "| Blank, Uhhh, Wait, First, What, Ready, Right,         |" \
             "\n| Yes, Nothing, Left, Press, Okay, No, Middle           |"
        blnk = "| Wait, Right, Okay, Middle, Blank, Press, Ready,       |" \
            "\n| Nothing, No, What, Left, Uhhh, Yes, First             |"
        nthng = "| Uhhh, Right, Okay, Middle, Yes, Blank, No,            |" \
                "\n| Press, Left, What, Wait, First, Nothing, Ready        |"
        yes = "| Okay, Right, Uhhh, Middle, First, What, Press,        |" \
            "\n| Ready, Nothing, Yes, Left, Blank, No, Wait            |"
        what = "| Uhhh, What, Left, Nothing, Ready, Blank, Middle,      |" \
            "\n| No, Okay, First, Wait, Yes, Press, Right              |"
        uhhh = "| Ready, Nothing, Left, What, Okay, Yes, Night,         |" \
            "\n| No, Press, Blank, Uhhh, Middle, Wait, First           |"
        left = "| Right, Left, First, No, Middle, Yes, Blank,           |" \
            "\n| What, Uhhh, Wait, Press, Ready, Okay, Nothing         |"
        right = "| Yes, Nothing, Ready, Press, No, Wait, What,           |" \
                "\n| Right, Middle, Left, Uhhh, Blank, Okay, First         |"
        middl = "| Blank, Ready, Okay, What, Nothing, Press, No,         |" \
                "\n| Wait, Left, Middle, Right, First, Uhhh, Yes           |"
        ok = "| Middle, No, First, Yes, Uhhh, Nothing, Wait,          |" \
            "\n| Okay, Left, Ready, Blank, Press, What, Right          |"
        wait = "| Uhhh, No, Blank, Okay, Yes, Left, First,              |" \
            "\n| Press, What, Wait, Nothing, Ready, Right, Middle      |"
        press = "| Right, Middle, Yes, Ready, Press, Okay, Nothing,      |" \
                "\n| Uhhh, Blank, Left, First, What, No, Wait              |"
        you = "| Sure, You Are, Your, You're, Next, Uh Huh, UR,        |" \
            "\n| Hold, What?, You, Uh Uh, Like, Done, U                |"
        youar = "| Your, next, Like, Uh Huh, What?, Done, Uh Uh,        |" \
                "\n| Hold, You, U, You're, Sure, UR, You Are              |"
        your = "| Uh Uh, You Are, Uh Huh, Your, Next, UR, Sure,         |" \
            "\n| U, You're, You, What?, Hold, Like, Done              |"
        youre = "| You, You're, UR, Next, Uh Uh, You Are, U,                |" \
                "\n| Your, What?, Uh Huh, Sure, Done, Like, Hold             |"
        ur = "| Done, U, UR, Uh Huh, What?, Sure, Your,               |" \
            "\n| Hold, You're, Like, Next, Uh Uh, You Are, You         |"
        u = "| Uh Huh, Sure, Next, What?, You're, UR, Uh Uh,         |" \
            "\n| Done, U, You, Like, Hold, You Are, Your               |"
        uhhuh = "| Uh Huh, Your, You Are, You, Done, Hold, Uh Uh,        |" \
                "\n| Next, Sure, Like, You're, UR, U, What?                |"
        uhuh = "| UR, U, You Are, You're, Next, Uh Uh, Done,            |" \
            "\n| You, Uh Huh, Like, Your, Sure, Hold, What?            |"
        whatq = "| You, Hold, You're, Your, U, Done, Uh Uh,              |" \
                "\n| Like, You Are, Uh Huh, UR, Next, What?, Sure          |"
        done = "| Sure, Uh Huh, Next, What?, Your, UR, You're,          |" \
            "\n| Hold, Like, You, U, You Are, Uh Uh, Done              |"
        nxt = "| What?, Uh Huh, Uh Uh, Your, Hold, Sure, Next,         |" \
            "\n| Like, Done, You Are, UR, You're, U, You               |"
        hold = "| You Are, U, Done, Uh Uh, You, UR, Sure,               |" \
            "\n| What?, You're', Next, Hold, Uh Huh, Your, Like        |"
        sure = "| You Are, Done, Like, You're, You, Hold, Uh Huh,       |" \
            "\n| UR, Sure, U, What?, Next, Your, Uh Uh                 |"
        like = "| You're, Next, U, UR, Hold, Done, Uh Uh,               |" \
            "\n| What?, Uh HUh, You, Like, Sure, You Are, Your          |"


        def steptwo(x):
            if x == "ready":
                print(rdy)
            elif x == "first":
                print(frst)
            elif x == "no":
                print(no)
            elif x == "blank":
                print(blnk)
            elif x == "nothing":
                print(nthng)
            elif x == "yes":
                print(yes)
            elif x == "what":
                print(what)
            elif x == "uhhh":
                print(uhhh)
            elif x == "left":
                print(left)
            elif x == "right":
                print(right)
            elif x == "middle":
                print(middl)
            elif x == "okay":
                print(ok)
            elif x == "wait":
                print(wait)
            elif x == "press":
                print(press)
            elif x == "you":
                print(you)
            elif x == "you are":
                print(youar)
            elif x == "your":
                print(your)
            elif x == "you're":
                print(youre)
            elif x == "ur":
                print(ur)
            elif x == "u":
                print(u)
            elif x == "uh huh":
                print(uhhuh)
            elif x == "uh uh":
                print(uhuh)
            elif x == "what?":
                print(whatq)
            elif x == "done":
                print(done)
            elif x == "next":
                print(nxt)
            elif x == "hold":
                print(hold)
            elif x == "sure":
                print(sure)
            elif x == "like":
                print(like)
            else:
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("| Oops! That wasn't a valid input. Try again...         |")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print("|                    WHO'S ON FIRST                     |")
        print("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+")
        print('| Type "exit" to exit.                                  |')
        print("+-------------------------------------------------------+")
        disword = str(input("| Display word: "))
        if disword == "ur":
            print("+=======================================================+")
            print(tl)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "yes":
            print("+=======================================================+")
            print(ml)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "nothing":
            print("+=======================================================+")
            print(ml)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "led":
            print("+=======================================================+")
            print(ml)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "they are":
            print("+=======================================================+")
            print(ml)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == " ":
            print("+=======================================================+")
            print(bl)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "reed":
            print("+=======================================================+")
            print(bl)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "leed":
            print("+=======================================================+")
            print(bl)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "they're":
            print("+=======================================================+")
            print(bl)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "first":
            print("+=======================================================+")
            print(tr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "okay":
            print("+=======================================================+")
            print(tr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "c":
            print("+=======================================================+")
            print(tr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "blank":
            print("+=======================================================+")
            print(mr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "read":
            print("+=======================================================+")
            print(mr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "red":
            print("+=======================================================+")
            print(mr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "you":
            print("+=======================================================+")
            print(mr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "your":
            print("+=======================================================+")
            print(mr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "you're":
            print("+=======================================================+")
            print(mr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "their":
            print("+=======================================================+")
            print(mr)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "first":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "display":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "says":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "no":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "lead":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "hold on":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "you are":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "there":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "see":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "cee":
            print("+=======================================================+")
            print(br)
            print("+=======================================================+")
            buttword = str(input("| Button word: "))
            print(steptwo(buttword))
            state += 1
        elif disword == "exit":
            state = 6
        else:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("| Oops! That wasn't a valid input. Try again...         |")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
