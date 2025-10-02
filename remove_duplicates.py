def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
        nums[i] = nums[j]
        
    return i + 1 

arr = list(map(int, input("Enter array elements").split()))
arr.sort()
length = removeDuplicates(arr)

print("Unique Length:", length)
print("Array after removing duplicates:", arr[:length])
    