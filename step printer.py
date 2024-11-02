# first we ask the users for the two numbers 
a = input('enter first number :')
b = input('enter second number :')
# now we ask the number for the step 
c = input('now enter the step :')
if int(a) <= int(b) :
    while int(a) <= int(b) :
        print(a)
        a = int(a) + int(c)
else :
    while int(a) >= int(b) :
        print(a)
        a = int(a) - int(c)