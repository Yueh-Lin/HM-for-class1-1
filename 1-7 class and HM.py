another way of doinf the homework:

score=list
score = [["A",100]["B",90]["C",80]["D",70]["E",60]]

max=0
for c in score:
    max=score[c]
    max=score[c-1]
      
    
min=101

for d in score:
    min=score[d]
    min=score[d-1]
    
2. using computer to calculate.

def add3(a,b,c):
    ans = a + b + c
    return ans
x = add3 (5,6,7)
print(x) 

def add3(a,b,c):
    ans = a / b + c
    return ans
x = add3 (9,3,7)
print(x) 

def add3(a,b,c):
    ans = a * b + c
    return ans
x = add3 (5,6,7)
print(x) 

preview today's homework:'
data = [90,87,65,78]
max=max(data)
min=min(data)
sum=sum(data)

print('最大數是：',max)
print("最小數是：",min)
print("總和是：",sum) 

print(sum/4)

Today's homework:
    
Charlie=input ('What is Charlie score?')
Evelyn=input ('What is Evelyn score?')
Mehta=input('what is Mehta score?')


Charlie=int(Charlie)
Evelyn=int(Evelyn)
Mehta=int(Mehta)

data = [90,87,65]
max=max(data)
min=min(data)
sum=sum(data)

print('最大數是：',max)
print("最小數是：",min)
print("總和是：",sum) 

print(sum/4)