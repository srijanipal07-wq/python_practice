#Find the prime numbers 
N = int(input("Enter a number: "))
flag = 0
for num in range(2, N ):
    if N % num == 0:
        flag = 1
        break
if flag == 0:
    print(N, "is a prime number.")
else:
    print(N, "is not a prime number.")