def bubble_sort(nums):
    nums1=nums[::]
    if nums1:
        for k in range(len(nums1)):
            for i in range(len(nums1)-1):
                if nums1[i]>nums1[i+1]:
                    nums1[i],nums1[i+1]=nums1[i+1],nums1[i]
        return nums1
    else:
        return []
    
def insertion_sort(nums):
    nums1=nums[::]
    for i in range(len(nums1)-1):
        if nums1[i]>nums1[i+1]:
            while nums1[i]>nums1[i+1]:
                nums1[i],nums1[i+1]=nums1[i+1],nums1[i]
                if i>0:
                    i=i-1
    return nums1

def min_num(nums):
    smol=10**10
    order=0
    for i in range(len(nums)):
        if nums[i]<smol:
            smol=nums[i]
            order=i
    return order,smol

def selection_sort(nums):
    nums1=nums[::]
    nums2=[]
    f=0
    for i in range(len(nums)):
        order,num=min_num(nums1)
        nums2.append(num)
        nums1.pop(order)
        f+=1
    return nums2

a=[2,7,3,1,0,5,4,6,4,3,1,0,-7]
#print(insertion_sort(a),selection_sort(a))
#     python -m src.lab07.sorting