name = 'Meet'

print(len(name))

print(name.endswith('eet'))
print(name.startswith('m'))
print(name.count('m'))

#____________________________________________   

#it will help to change string still main string is immutabel

table = str.maketrans('aeiou','12345')
s = "Hello world chhe mara taraf thi"
print(s.translate(table))

#to swap the case of string

print(name.swapcase())