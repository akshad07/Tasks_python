#1. Write a Python program to sum all the items in a list.


x = [int(x) for x in input("Enter multiple value Using Commas : ").split(",")]
sum = 0
for i in x:
     sum +=i

print("Sum of n Number of list :- ",sum)
print("........")
