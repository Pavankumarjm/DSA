def reverse_int(n):
    sign = -1 if n < 0 else 1
    n = n * sign 
    
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    
    return sign * rev


print(reverse_int(123)) 
print(reverse_int(-456))  