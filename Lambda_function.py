square=lambda x:x*x
print(square(5))
x=lambda a,b,c:a+b+c
print(x(1,2,3))
numbers=[1,2,3,4,5]
squared_numbers=list(map(lambda x:x*x,numbers))
print(squared_numbers)
