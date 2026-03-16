def RemoveDuplicates(nums):
    k=1
    for i in range(nums):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1
    return k        