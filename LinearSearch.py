arr=[30,20,10,60,7,90,4]
key=7
found=False

for i in range(len(arr)):
    if arr[i]==key:
        print("Found",i)
        found = True
        break
    if not found:
        print("not found")