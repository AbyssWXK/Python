str = input()
n = int(str)
i = 0
while (n != 1):
    if n%2==0:
        n=n/2
    else:
        n=3*n+1
        n=n/2
    i=i+1
print(i)

