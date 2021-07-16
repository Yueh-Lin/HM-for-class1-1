lesson:
date = {"today date":'7/15','yesterday date':'7/14','tomorrow date':'7/16'}  
print(date)

for k in date.keys():
    print(k)
    
for v in date.values():
    print(v)

t = 'week date' in date
print(t)    

for k, v in date.items():
    print(k,v) 
    

HM:
buy = {'A001':'小熊軟糖','A002':'冰棒','A004':'王子麵','A006':'汽水'}
print(buy)  

for k, v in buy.items():
    print(k,v) 

x = 'week date' in buy
print(x)

x=input("what so you want to buy today?")

o ='Guinea pig' in buy
print(x)  

A='A001'
if A == x:
    print("小熊軟糖 20$")
    
B='A002'
if B == x:
    print("冰棒 25＄")
        
C='A004'
if C == x:
    print("王子麵 10$")    

D='A006'
if D == x:
    print("汽水 30$")
    