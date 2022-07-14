#SNAKE WATER GUN OR STONE PAPER SCISSORS GAME
import random
def game(comp,you):
    if(comp==you):
        return None
    
    if(comp=='s'):
        if(you=='g'):
            return True
        else:
            return False
    if(comp=='w'):
        if(you=='s'):
            return True
        else:
            return False
    if(comp=='g'):
        if(you=='w'):
            return True
        else:
            return False
        
print("COMP TURN:CHOOSE SNAKE(s) WATER(w) OR GUN(g)")
randomnumber=random.randint(1,3)
if(randomnumber==1):
    comp='s'
elif(randomnumber==2):
    comp='w'
else:
    comp='g'

you=input("YOUR TURN:CHOOSE SNAKE(s) WATER(w) OR GUN(g)")

print("You Chose :"+you)
print("Comp Chose :"+comp)

result=game(comp,you)
if(result==None):
    print("MATCH IS TIED")
elif result:
    print("YOU WIN ! CONGRATS.....")
else:
    print("YOU LOSE BETTER LUCK NEXT TIME")
