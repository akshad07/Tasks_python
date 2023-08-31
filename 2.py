# 2. Write a Python program to multiply all the items in a list.

x = [int(x) for x in input("Enter multiple value Using Commas : ").split(",")]
sum = 1
for i in x:
    sum = sum * i


print("Multiply of n Number of list :- ", sum)
