#find missing number in an array 

def missing_no(arr):
    first=min(arr)
    last=max(arr)
    for i in range(first,last+1):
        if i not in arr:
            print(i)
arr=list(map(int,input("enter the values:").split()))
missing_no(arr) 
