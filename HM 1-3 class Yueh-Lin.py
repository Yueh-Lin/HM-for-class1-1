import random
num=random.randint (1,10)

x=input("what is your number?")

num=int(num)
x=int(x)
    
while x != num:
    print("you are wrong")
    x=input("what is your number?")  
    x=int(x)

print("you got it") 

if num != x * 5:
    print("no more chance")