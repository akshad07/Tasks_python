#9. Write a Python script to add a key to a dictionary.

Dict = {1:'A',2:'K'}
print("Previous Dict : ",Dict)
count = len(Dict)

Dict[count+1] = input("Enter a Key to Add into Dict : ")
print("Current Dict : ",Dict)