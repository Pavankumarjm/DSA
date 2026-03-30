def contains_duplicates(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == lst[j]:
                return True
    return False

numbers = [1, 2, 3, 4, 2]
print(contains_duplicates(numbers))  # True