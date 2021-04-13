#Project
#Student Information System
#Madidis Hannah Jane

import csv

STD_attributes = ['Name', 'ID Number', 'Year Level', 'Gender', 'Course']
StudentDatabase = 'Studentdata.csv'

def Main():
    print("--------------------------------------------")
    print("    MSU-IIT STUDENT INFORMATION SYSTEM      ")
    print("--------------------------------------------")
    print("1. ADD NEW ")
    print("2. DISPLAY STUDENTS")
    print("3. SEARCH STUDENT")
    print("4. EDIT STUDENT")
    print("5. DELETE STUDENT")
    print("6. EXIT")
    print()

def AddStudent():
    print("---------------------")
    print("    ADD STUDENT      ")
    print("---------------------")
    
    global STD_attributes 
    global StudentDatabase 
    
    STD_data = []
    for field in STD_attributes :
        value = input("Enter " + field + ": ")
        STD_data.append(value)
        
    with open(StudentDatabase , "a", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([STD_data])
    
    print("Wow! Data added successfully!")
    input("Press any key to continue:")
    return

def ViewStd():
    global STD_attributes 
    global StudentDatabase 
    
    print("----------------------")
    print("     STUDENT LIST     ")
    print("----------------------")
    
    with open(StudentDatabase , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for x in STD_attributes :
            print( x, end = "\n")
        print("\n-------------------------------------------------")
        
        for row in reader:
            for item in row:
                print( item, end = "\n")
            print()        
    input("Press any key to continue:")

    
def SearchStd():
    global STD_attributes 
    global StudentDatabase 
    
    print("------------------------")
    print("     SEARCH STUDENT     ")
    print("------------------------")
    
    STD_ID = input("Enter ID Number:")
    with open(StudentDatabase , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if STD_ID == row[1]:
                    print("You found it!")
                    print("Name: ", row[0])
                    print("ID Number: ", row[1])
                    print("Year Level: ", row[2])
                    print("Gender: ", row[3])
                    print("Course: ", row[4])
                    break
        
        else:
            print("Oops! This Student does not exist!")
    input("Press any key to continue:")


# Edit student
def EditStd():
    global STD_attributes 
    global StudentDatabase 
    
    print("------------------------")
    print("     UPDATE STUDENT     ")
    print("------------------------")
    
    STD_ID = input("Enter ID Number of student you want to edit: ")
    Std_index = None
    Edit_data = []
    with open(StudentDatabase , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if STD_ID == row[1]:
                    Std_index = counter
                    print("Student Found: at index ", Std_index)
                    STD_data = []
                    for field in STD_attributes :
                        value = input("Enter " + field + ": ")
                        STD_data.append(value)
                    Edit_data.append(STD_data)
                else:
                    Edit_data.append(row)
                counter += 1
                
    # Check if the record is or not found
    if Std_index is not None:
        with open(StudentDatabase , "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(Edit_data)
    
    else:
        print("Sorry! ID Number could not be found\n")
    p   
    input("Press any key to continue:")
    
def DeleteStd():
    global STD_attributes 
    global StudentDatabase 
    
    print("------------------------")
    print("      DELETE STUDENT    ")
    print("------------------------")
    
    STD_ID = input("Enter ID Number of student to remove: ")
    Std_Found = False
    Edit_data = []
    with open(StudentDatabase , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if STD_ID != row[1]:
                    Edit_data.append(row)
                    counter += 1
                else:
                    Std_Found = True
    
    if Std_Found is True:
        with open(StudentDatabase , "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(Edit_data)
        print("ID Number:\n ", STD_ID, "Removed successfully!")
    
    else:
        print("Oops! ID Number not found")
    
    input("Press any key to continue:")


# Main
while True:
    Main()
    
    choice = input("What do you want to do?Please Enter the Number:")
    if choice == '1':
        AddStudent()
    elif choice == '2':
        ViewStd()
    elif choice == '3':
        SearchStd()
    elif choice == '4':
        EditStd()
    elif choice == '5':
        DeleteStd()
    else:
        break


# Termination
print("********************************************************************")
print("*  THE SYYTEM HAS BEEN TERMINATED,THANK YOU FOR USING THE SYSTEM!  *")
print("********************************************************************")



