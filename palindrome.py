
    
def palindrome_check(string):
    if string==string[::-1]:
    
        print('palindrome')
    else:
         print("not palindrome")
   
string=input("enter the satring:")
 
palindrome_check(string)