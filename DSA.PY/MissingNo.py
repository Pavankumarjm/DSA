arr = [1, 2, 4, 5]

n = 5 

total = n * (n + 1) // 2
arr_sum = sum(arr)

missing = total - arr_sum

print("Missing number is:", missing)