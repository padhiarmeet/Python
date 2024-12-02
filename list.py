arr = ['one','apple','aaple','cat']

# arr[1] = 1212

# arr.append("l0l")

arr.sort(reverse=True) #You can sort list in reverse for that you have to use reverse = True...
arr.sort(key=len)  #It will sort list according key

# arr.reverse()

# arr.pop()

print(sorted(arr)) #Your can also sort List for temperary....

del arr[0]  # to remove wanted elemnt..

squre = [x ** 2 for x in range(5)]  # you can dinamacially assingn value..

print(f"this is value of squre {squre}")

print(arr.count('one'))  # gives occurence of input..

arr.clear()
print(arr)