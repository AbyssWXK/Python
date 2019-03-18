import random
x = 0
y = 0
for i in range(100000):
    a = random.randint(0,1)
    b = random.randint(0,1)
    if a ==0 or b==0:
        y = y + 1
        if a==0 and b==0:
            x= x+1
print(x)
print(y)
print(x/y)
