def arm_strong(num):
    Temp=num
    length=len(str(num))
    sum=0
    while num > 0:
        digit=num%10
        sum=sum+digit**length
        num=num//10
    if(sum==Temp):
        print(f"{Temp} is an armstrong number")
    else:
        print(f"{Temp} is not an armstrong number")

num=int(input("enter the number:"))
arm_strong(num)