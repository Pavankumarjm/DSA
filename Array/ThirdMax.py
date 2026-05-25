arr = [10, 4, 3, 50, 23, 90]

first = second = third = -9999

for i in arr:
    if i > first:
        third = second
        second = first
        first = i

    elif i > second:
        third = second
        second = i

    elif i > third:
        third = i

print("Third Maximum Number:", third)