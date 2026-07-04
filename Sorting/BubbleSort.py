arr=[50,20,10,75,23,55,4]
n=len(arr)
for i in range (n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr) 