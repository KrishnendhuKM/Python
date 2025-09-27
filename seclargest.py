"""nums = list(map(int, input().split()))
second_largest = list(set(nums))
if len(second_largest) < 2:
    print(-1)
else:
    second_largest.sort(reverse = True)
    print(second_largest[2])"""
    

def thirdlargest(arr):
       
    arr.sort()
    return arr[ - 2]

arr = list(map(int, input().split()))
print("2nd largest num is:" ,thirdlargest(arr))