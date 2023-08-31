import csv
contact = "contact_data.csv"
contact_field = ['id','name','email','gender','dob','address','mobile']

def view():
    print("----Contacts Record----")
    with open('contact_data.csv', mode="r") as csv_file:
      reader = csv.reader(csv_file) 

      for item in reader:
        print("......................................................................................................")
        print(item)
    input("\n""Press Enter To Continue")    

def add():
    print("-------------------------")
    print("Add Contact Details")
    print("-------------------------")
    contact_data=[]
    for field in contact_field:
        value = input("Enter " + field +": ")
        contact_data.append(value)   
    add2('contact_data.csv',contact_data)
      
    input("\n""Contact Added Successfully""\n""\n""Press Enter To Continue")    

def add2(file_name, list):
   
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(list)
       
def delete():
    print("-------------------------")
    updatedlist=[]
    with open("contact_data.csv",newline="") as f:
      reader=csv.reader(f)

      id=input("Enter the ID of Contact to Delete : ")
      contactid= False
      for row in reader:            
                if row[0]!=id: 

                    updatedlist.append(row)
                else:
                    contactid=True
      if contactid is True:
          updatefile(updatedlist)
      else:
          print("\n""ID Not Found")    
         
    
      input("\n""Press Enter To Continue")                 
    

def updatefile(updatedlist):
    with open("contact_data.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
        print("\n""Contact Has Been Deleted")

    
while True:
    print("\n""Enter number to select option")
    print("1. List Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Exit")
    print("\nEnter Number :- ")
    val = int(input())
    if val == 1:
        view()
    elif val == 2:
        add()
    elif val == 3:
        delete()
    elif val == 4:
        break
    else:
        print("Entered Invalid value")

print("Thank You For Using..!")
