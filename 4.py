#4. Write a Python program to get the Smallest number from a list.

x = [int(x) for x in input("Enter multiple value Using Commas : ").split(",")]
Smallest = x[0]

for i in x:
    val = i
    if Smallest >i:
        Smallest=i
print("Smallest number from a list :",Smallest)
