def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [10, 50, 1,49, 4, 90, 65,3]

sorted_numbers = quick_sort(numbers)

print("Sorted array:", sorted_numbers)