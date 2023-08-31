#7. Write a Python program to count the number of characters (character frequency) in a string.
 
str = input("Enter String to number of characters : ")
for i in str:
    counter = str.count(i)
    print("Count of "+i+" = ",counter)
