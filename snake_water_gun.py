import random
def game(b,c):
    if b=="s" and c=="w":
        print("player won the game")
        print("you chose ",b ,"   computer chose   ", c)
    elif b=="w" and c=="g":
        print("player won the game")
        print("you chose ",b ,"   computer chose   ", c)
    elif b=="g" and c=="s":
        print("player won the game ")
        print("you chose ",b ,"   computer chose   ", c)
    elif b==c:
        print("draw the match has been tied ")
        print("you chose ",b ,"   computer chose   ", c)
    else :
        print("the computer won the game and chose",c)
        print("you chose ",b ,"   computer chose   ", c)
    #pass

rn=random.randint(1,3)
if rn==1:
    c="s"
elif rn==2:
    c="w"
elif rn==3:
    c="g"

print("player is against computer ")
a=input("enter snake(s), water (w) or gun (g)        ")
game(a,c)
