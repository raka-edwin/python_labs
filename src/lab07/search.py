def linear_search(nums, x):
    if len(nums)==0:
        return -1
    else:
        for i in range(len(nums)):
            if nums[i]==x:
                return i
        return -1
def binary_search(sorted_nums, x):
    order=len(sorted_nums)
    k=0
    lo=0
    hi=order-1
    mid=order-1//2
    if len(sorted_nums)==0 or x>sorted_nums[-1] or x<sorted_nums[0]:
        return -1
    elif sorted_nums[0]==x:
        return 0
    else:
        while k==0:
            mid=(lo+hi)//2
            if lo+1==hi and lo==mid:
                return -1
            elif sorted_nums[mid]==x:
                return mid
            elif sorted_nums[mid]>x:
                hi=mid
            elif sorted_nums[mid]<x:
                lo=mid
            
def two_sum_brute(nums, target):
    if len(nums)==0:
        return None
    else:
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
    return None

def two_sum_fast(nums,target):
    seen = {}
    for index, num in enumerate(nums):
        a=target-num
        if a in seen:
            return [seen[a], index]
        seen[num] = index
    return None
#print(two_sum_fast([1,2,3,4,5,6,7,8,9,10],13))
#     python -m src.lab07.search