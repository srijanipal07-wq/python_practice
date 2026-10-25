# magic number concept using for loop
n=int(input("Enter the number: "))
square=n**2
sum=0
for i in str(square):
    sum+=int(i)
if sum==n:
    print(n,"is a magic number:")
else:
    print(n,"is not a magic number:")
#magic number concept using while loop
n=int(input("Enter the number: "))  
square=n**2
sum=0
while square>0:
    digit=square%10
    sum+=digit
    square//=10 
if sum==n:
    print(n,"is a magic number:")
else:
    print(n,"is not a magic number:")