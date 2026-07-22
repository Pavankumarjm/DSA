arr=[30,20,11,70,7,110,6]
key=7
found=False

for i in range(len(arr)):
    if arr[i]==key:
        print("Found",i);
        found = True
        break
    if not found:
        print("not found");