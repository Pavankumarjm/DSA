arr=[50,10,40,65,25,35,2]
n=len(arr)
for i in range (n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)            