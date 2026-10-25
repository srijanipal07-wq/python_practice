num_str = input("Enter the number: ")
n = int(num_str)

total_sum = 0


for digit_char in num_str:
    digit = int(digit_char)
    

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i 
        

    total_sum += fact


if total_sum == n:
    print(n, "is a krishnamurthy number.")
else:
    print(n, "is not a krishnamurthy number.")