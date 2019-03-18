with open('pi.txt') as file_object:
    lines=file_object.readline()
pi_string=''
for line in lines:
    pi_string+=line.rstrip()
birthday = input("Enter your birthday:")
#for pi_numb in pi_string:
    #for birth_numb in birthday:
       # if pi
#print(type(birthday))
birthday='960903'
print(pi_string)
str(pi_string)
#print(pi_string)
local = pi_string.find(birthday)
print(local)