def pyout(strnum):
  if strnum=='1':
    print('yi', end='')
  elif strnum=='2':
    print('er', end='')
  elif strnum=='3':
    print('san', end='')
  elif strnum=='4':
    print('si', end='')
  elif strnum=='5':
    print('wu', end='')
  elif strnum=='6':
    print('liu', end='')
  elif strnum=='7':
    print('qi', end='')
  elif strnum=='8':
    print('ba', end='')
  elif strnum=='9':
    print('jiu', end='')
  elif strnum=='0':
    print('ling', end='')

str = input()
sum = 0
for char in str:
  sum = sum + int(char)

strsum = '%d'%sum
len = len(strsum)
x = 0
while x<len:
  pyout(strsum[x])
  x=x+1
  if x==len:
    break
  print(' ', end='')
