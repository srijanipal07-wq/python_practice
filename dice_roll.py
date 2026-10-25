import random
n=int(input("Enter the number of times you want to roll the dice: "))
total_sum=0
for i in range(n):
    roll=random.randint(1,6)
    print(f"Roll {i+1}: {roll}")
    total_sum+=roll
print(f"Total sum of rolls: {total_sum}")
