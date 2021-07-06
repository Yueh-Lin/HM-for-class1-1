num=input ('num score?')
eng=input ('eng score?')

eng=int(eng)
num=int(num)

if eng >= 90 and num >= 90:
    print("have gift")
    
if eng < 90 and num < 90:
    print("Punishment")
    
elif eng < 90 and num > 90:
    print('try more')