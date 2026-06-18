arr = [1, 2, 3, 4, 5]

flag = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        flag = False
        break

if flag:
    print("Array is Sorted")
else:
    print("array is not sorted");