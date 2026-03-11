num = 6
count = 0

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            count = count + 1

    if count == 0:
        print("Number is prime")
    else:
        print("Not a prime number")
else:
    print("Not a prime number")