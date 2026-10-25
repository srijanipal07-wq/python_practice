num_str=input("Enter the number: ")
n=int(num_str)
num_digit = len(num_str)
sum=0
temp=n      
while temp>0:
    digit=temp%10
    sum=sum+digit**num_digit
    temp//=10
if n==sum:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")