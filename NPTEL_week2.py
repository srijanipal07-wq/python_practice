def intreverse(n):
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    return reverse
print(intreverse(12345))  # Output: 54321
def matched(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False  
    return count == 0
print(matched("((()))"))  # Output: True
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False

def sumprimes(l):
    total_sum = 0
    for num in l:
        if is_prime(num):
            total_sum += num
    return total_sum
print(sumprimes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 17
