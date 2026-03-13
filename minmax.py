arr=[3,7,2,9,4]
max=arr[0]
min=arr[0]
for num in arr:
    if num>max:
        max=num
    if num<min:
        num=min
print("max",max)
print("min", min)        