#5. Write a Python program to count the number of strings from a given list of strings. 
#   The string length is 2 or more and the first and last characters are the same.

x = [(x) for x in input("Enter multiple Strings Using Commas : ").split(",")]  
count = 0
for a in x:
    str = a
    for b in a:
        if len(a)>1:
            if str[0]==str[-1]:
               count = count +1
               break

print("The Count of strings which First and Last Character is same :   ",count)