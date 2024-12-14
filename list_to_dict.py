#Conversion of two list into Dictionary

def list_to_dict(l1,l2):
    
    res=dict(zip(l1,l2))  #zip(l1, l2) pairs the elements of l1 and l2 into tuples->(1, 'a'), (2, 'b'), (3, 'c') 
                        #The dict() function will convert the pairs of tuples into key-value pairs in a dictionary {1: 'a', 2: 'b', 3: 'c'}
    print(res)


l1=list(map(int,input("enter the key val (seperated by space):").split()))
l2=input("enter the pair values:").split()
result=list_to_dict(l1,l2)
print(result)