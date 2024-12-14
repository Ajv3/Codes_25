
# finding common letters btw  two strings


def common_letters(str1,str2):

 #str into set to remove duplicates

    s1=set(str1) 
    s2=set(str2)

# Find common letters

    cmn=s1&s2 

    print(sorted(cmn))

str1=input("enter the first string:")
str2=input("enter the second string:")
result=common_letters(str1,str2)
print(result)
    