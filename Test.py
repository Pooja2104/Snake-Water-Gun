import random


def GameWin(Comp, You):
    if Comp == You:
        return None
    elif Comp == 'S':
        if You == 'W':
            return False
        elif You == 'G':
            return True
    elif Comp == 'W':
        if You == 'G':
            return False
        elif You == 'S':
            return True
    elif Comp == 'G':
        if You == 'S':
            return False
        elif You == 'W':
            return True

Comp = print("Comp Turn : Snake(S) Water(W) or Gun(G)?")
RandomNo = random.randint(1,3)
if RandomNo == 1:
    Comp = 'S'
elif RandomNo == 2:
    Comp = 'W'
elif RandomNo == 3 :
    Comp = 'G'

You = input("Your Turn : Snake(S) Water(W) or Gun(G)?")

a = GameWin(Comp,You)

print(f"Computer choose {Comp}")
print(f"You choose {You}")

if a == None:
    print('Game is a tie!')
elif a:
    print("You Win")
else:
    print("You loose")