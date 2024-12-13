""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]."""

#method 1 [brute method] -->Time Complexity: O(n^2)

"""def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]

nums=list(map(int,input("enter the values space seperated:").split()))
target=int(input("enter the target:"))
result=two_sum(nums,target)
print(result)"""


#method 2 using dictionary --> Time Complexity:O(n) 

def two_sum(nums,target):
    dict={}
    for i,num in enumerate(nums):
        differ=target-num
        if differ in dict:
            return[dict[differ],i]
        dict[num]=i
nums=list(map(int,input("enter the values seperated by space:").split()))
target=int(input("enter the target:"))
result=two_sum(nums,target)
print(result)        
