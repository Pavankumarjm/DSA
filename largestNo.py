arr = [10, 45, 23, 89, 12]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i


print("Largest number:", largest)