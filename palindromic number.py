#Palindromic Number 
n=int(input("Enter a number: "))
if str(n)==str(n)[::-1]:
    print(n,"is a Palindromic Number")
else:
    print(n,"is not a Palindromic Number")