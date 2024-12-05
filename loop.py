for value in range(1,5): # it will not print 5(Last value)
    print(value)
for value in range(6):
    print(value)

numbers = list(range(6))
print(numbers)

even = list(range(0,11,4))
print(even)

#to print squre of 1 to 10
squres = []

for value in range(1,11):
    squre = value ** 2
    squres.append(squre)

print(squres)

name = ['a','b','c','d','e','f'];
for i in range(0,9):
    print(name[0:i])

