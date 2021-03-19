numbers=list(range(1,11))
print("The first three items in the list are:")
print(numbers[0:3])

print("Three items from the middle of the list are:")
length=len(numbers)
half=int(length/2)
print(numbers[half:half+3])

print("The last three items in the list are:")
print(numbers[-3:])
