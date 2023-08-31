#3. Write a Python program to get the largest number from a list.

x = [int(x) for x in input("Enter multiple value Using Commas : ").split(",")]
largest = x[0]

for i in x:
    val = i
    if largest <i:
        largest=i
print("largest number from a list :",largest)
