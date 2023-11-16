import sqlite3                              #Import the SQLite3 package and connect our database and cursor
con = sqlite3.connect('travis.db')
mycursor = con.cursor()
#creating the sql query that is used to create the database
table_query = "CREATE TABLE IF NOT EXISTS `client_data`(`unique_id` INTEGER PRIMARY KEY AUTOINCREMENT,`Fname` TEXT,`Lname` TEXT,`contact_number` TEXT,`blood_type` TEXT);"
#Executing the SQL query
mycursor.execute(table_query)
con.commit()
#Registration Function
def donor_register():
    try: #We use a try statement to do all the code and if it doesnt work properly we print an error
        #getting the user to input all the information we need
        pname = input("insert Patient Name\n")
        psurname = input("insert Patient Surname\n")
        pcontact_number = input("insert Patient Contact Number\n")
        pblood_type = input("insert Patient Blood Type\n")
        #we tell the program that we are using the global variables for mycuror and con and not creating our own local ones
        global mycursor
        global con
        #create our query and get our arguments that will go into the query
        query = "INSERT INTO `client_data`(Fname,Lname,contact_number,blood_type)VALUES(?,?,?,?)"
        args = (pname,psurname,pcontact_number,pblood_type)
        #Execute the query with the arguments
        mycursor.execute(query,args)
        con.commit()

        print("DONOR ADDED SUCCESFULLY \n")
        #If any errors occured during this process it will not run any of the code and it will print an error
    except Exception:
        print("ERROR OCCURED \n")
    #at the end it will go back to our run function which is our main menu 
    finally:
        run()


#update patient information function
def donor_update():
    try: #We tell the program that we are going to be using the global variables for mycursor and con
        global mycursor
        global con
        #get users contact number
        user_contact_number = input("Enter your current contact number \n")

        #find out what the user would like to update
        user_input = int(input('''
                        Please input what you would like to update:
                        1. First Name
                        2. Surname
                        3. Contact Number
                        '''))
        #We have 3 if statements that will check to see which one the user would like to change
        # For each of them we get the new user input and then create our query based on his / her contact number. Each individual has a unique contact number so we use that to find their information in the table
        # so we use our query with "WHERE" to match contact number with the one they inputed already. we then build our query and put in our arguments and execute the sql statement followed by a print message
        if user_input == 1:
            new_name = input("Enter new first name \n")
            query = "UPDATE `client_data` SET `Fname` = ? WHERE `contact_number` = ?;"
            args = (new_name,user_contact_number)
            mycursor.execute(query,args)
            con.commit()
            print(f'UPDATED FIRST NAME \n')

        elif user_input == 2:
            new_surname = input("Enter new surname \n")
            query = "UPDATE `client_data` SET `Lname` = ? WHERE `contact_number` = ?;"
            args = (new_surname,user_contact_number)
            mycursor.execute(query,args)
            con.commit()
            print(f'UPDATED LAST NAME \n')

        elif user_input == 3:
            new_number = input("Enter new contact number \n")
            query = "UPDATE `client_data` SET `contact_number` = ? WHERE `contact_number` = ?;"
            args = (new_number,user_contact_number)
            mycursor.execute(query,args)
            con.commit()
            print(f'UPDATED CONTACT NUMBER NAME \n')
    # Exception to catch any errors and report
    except Exception:
        print("ERROR OCCURED")
    # go back to the main menu
    finally:
        run()
#Donor remove function
def donor_remove():
    try:    #global variables for mycursor and con not local
        global mycursor
        global con
        #get the users contact number so that it can be used to locate the users information in the database
        # then build our query to delete the users information based off its contact number
        remove_user = input("Enter User Contact Number you want to remove\n")
        query = "DELETE FROM `client_data` WHERE `contact_number` = ?;"
        args = (remove_user)
        #execute the sql query
        mycursor.execute(query,args)
        con.commit()
        #print our final message to say it was successful
        print(f'USER WITH CONTACT NUMBER {remove_user} HAS BEEN REMOVED SUCCESFULLY \n')
    #print error if it cannot remove user
    except Exception:
        print(f'ERROR OCCURED TRYING TO REMOVE USER {remove_user} \n')
    #back to main menu
    finally:
        run()
# display records function
def displayRecords():
    try: #global variables for mycursor and con not local
        global mycursor
        global con
        #Create our query to get all the data 
        query = "SELECT * FROM `client_data`;"
        # give our execute code a variable so we can just run it multiple times in a loop
        records = mycursor.execute(query)
        #give our data headings
        print(f'Unique ID | Username | Usersurname | ContactNumber | BloodType')
        #for loop to get the data out of our database and print them accordingly
        for data in records:
            print(f'{data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]}')
    # print error if cannot display data
    except Exception:
        print("ERROR OCCURED WHEN TRYING TO DISPLAY DATA \n")
    # back to main menu
    finally:
        run()
#main menu function that brings with a response variable that the user entered in the previous run function
def mainMenu(response):
    #if else statements to check which of the 5 options the user inputed and a error catch if its not 1 to 5 that will print a error and go back to the main menu else if correct it will run the function required
    if response == 1:
        donor_register()
    elif response == 2:
        displayRecords()
    elif response == 3:
        donor_update()
    elif response == 4:
        donor_remove()
    elif response == 5:
        print("GOODBYE ...")
    else:
        print("INVALID NUMBER \n")
        run()
        

# Our run function that will display the main menu for the user and ask for a user input 
def run():
    print('''
        1. Register Donor
        2. Display Records of all registered donors
        3. Update Existing Record
        4. Delete a Record
        5. Exit Program
        ''')
    # get user input
    input_response = int(input());
    # run the main menu function and send it the response it wanted
    mainMenu(input_response)


#executes the run function on start up of the program so it instantly goes to a mainmenu
run()