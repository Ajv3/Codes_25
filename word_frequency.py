def word_freq(str):

    list=str.split()  # Split the input string into a list of words based on whitespace

    dict={}

    for i in list: # Iterate through each word in the list of words

        if i  not in dict.keys():  # Check if the word is not already a key in the dictionary

            dict[i]=0

        dict[i]=dict[i]+1

    print(dict)

str=input("enter the words:")    
result=word_freq(str)
print(result)