num = int(input("Enter a number: "))
count=0
if num>1:
    for i in range(2, num):
        if (num%i)==0:
         count = count+1
        if count ==2:
           print("number is prime")
        else:
           print("Not a prime number")   