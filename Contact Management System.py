#import a package for useful regex methods
import re

#Use a nested dictionary to detail contact information
contacts = {
    "Contact_1": {"Name": "Joe Gloyd", "Phone Number": "(123) 456-7890", "Email": "joe@web.com", "Address": "123 Street City, ST 12345"}
}

#Function for adding contact information to the nested dictionary
def Add_Contact():
    #Request information for the new user contact
    contact_first_name = input("What is the new contacts first name? ")
    contact_last_name = input("What is the new contacts last name? ")

    #Capitalize the first and last name, then join them to be added to the contacts later
    contact_first_name = contact_first_name.capitalize()
    contact_last_name = contact_last_name.capitalize()
    contact_name = contact_first_name + " " + contact_last_name

    #Initiate a check for valid phone numbers
    valid_number = True
    #Request a 10-digit phone number for the new contact
    contact_number = input("What is the new contacts 10-digit phone number? ")
    #Iterate through the given input and check for non-digit characters
    for char in contact_number:
        if char.isdigit() == False:
            valid_number = False

    #If the phone number is not a 10-digit number, continue to prompt the user for a proper phone number
    while len(contact_number) != 10 or valid_number == False:
        print("I'm sorry, this is not a valid phone number.")
        #Reset the valid number check
        valid_number = True

        contact_number =input("Please enter a valid 10-digit phone number: ")

        #Trip the valid number check if there are any non-digits in the input
        for char in contact_number:
            if char.isdigit() == False:
                valid_number = False

    #Reformat the phone number for readability
    contact_number = f"({contact_number[0:3]}) {contact_number[3:6]}-{contact_number[-4:]}" 

    #Request the user provide a valid email address, checking if the email is formatted properly
    contact_email = input("What is the new contacts email? ")
    valid_email = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", contact_email)

    #If the email is not in the proper format, provide an example for the user and request again until a proper email is given
    while valid_email == None:
        print("Please provide a valid email address (example: email@web.com)")
        contact_email = input("What is the new contacts email? ")
        valid_email = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", contact_email)

    #Request the user provide an address for the new contact, any format will do
    contact_address = input("What is the new contacts address? ")

    #Update the nested dictionary with the new contact using the information the user provided
    new_contact_info = {"Name": contact_name, "Phone Number": contact_number, "Email": contact_email, "Address": contact_address}
    contacts.update({contact_number: new_contact_info})

#Function for editing contact information
def Edit_Contact():
    #Request the user to provide a name for the contact info they want to change
    edit_selection = input("What is the name of the contact you would like to edit? ")

    for i in contacts:
        if edit_selection.capitalize() in contacts[i]["Name"]:
            #Request the user to input which key they would like to edit the value for in the nested dictionary
            edit_selection = input(f"Would you like to edit {contacts[i]["Name"]}'s name, phone number, email, or address? ")
            break

    #When the user wants to edit a contacts name
    if edit_selection.lower() == "name":
        #Request user input to change the contacts name, format the input, update the contacts name, and provide the user with feedback
        contact_first_name = input("What is the contacts first name? ")
        contact_last_name = input("What is the contacts last name? ")

        contact_first_name = contact_first_name.capitalize()
        contact_last_name = contact_last_name.capitalize()
        contact_name = contact_first_name + " " + contact_last_name

        contacts[i].update({"Name": contact_name})
        print(f"Contacts name has been changed to {contact_name}!")

    #When the user wants to edit a contacts phone number
    elif edit_selection.lower() == "phone number":
        valid_number = True

        #Request a 10-digit phone number for the new contact
        contact_number = input("What is the new contacts 10-digit phone number? ")

        #Iterate through the given input and check for non-digit characters
        for char in contact_number:
            if char.isdigit() == False:
                valid_number = False

        #If the phone number is not a 10-digit number, continue to prompt the user for a proper phone number
        while len(contact_number) != 10 or valid_number == False:
            print("I'm sorry, this is not a valid phone number.")
            #Reset the valid number check
            valid_number = True

            contact_number =input("Please enter a valid 10-digit phone number: ")

            #Trip the valid number check if there are any non-digits in the input
            for char in contact_number:
                if char.isdigit() == False:
                    valid_number = False

        #Reformat the phone number for readability
        contact_number = f"({contact_number[0:3]}) {contact_number[3:6]}-{contact_number[-4:]}"
        #If the phone number was validated without issue, update the contacts phone number and provide feedback for the user
        if valid_number == True:
            contacts[i].update({"Phone Number": contact_number})
            print(f"{contacts[i]["Name"]}'s number has been changed!")

    #When the user wants to edit a contacts email address
    elif edit_selection.lower() == "email":
        #Request a new email input from the user and validate the formatting
        new_email = input(f"Please enter {contacts[i]["Name"]}'s new email address: ")
        valid_email = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", new_email)
        #If the format of the user input did not match an email address, provide feedback for the user
        if valid_email == None:
            print("I'm sorry, this is not a valid email address. Returning to main menu..")
        #If the format of the user input matches a typical email address, update the contacts email and provide feedback
        else:
            contacts[i].update({"Email": new_email})
            print(f"{contacts[i]["Name"]}'s email has been changed!")

    #When the user wants to edit a contacts physical address
    #Addresses vary quite a lot, just allow the user to enter in any input, they can always change it later
    elif edit_selection.lower() == "address":
        new_address = input(f"Please enter {contacts[i]["Name"]}'s new address: ")
        contacts[i].update({"Address": new_address})
        print(f"{contacts[i]["Name"]}'s address has been changed!")

    #Let the user know that they did not select an appropriate option and returnt to the main loop
    else:
        print("I'm sorry, that was not one of the options. Returning to main menu..")

#Function for deleting contacts
def Delete_Contact():
    #Request the user provide the name of the contact they want to delete
    contact_to_delete = input("What is the name of the contact you would like to delete? ")
    #Iterate through the nested dictionary, searching for a matching name
    for i in contacts:
        if contacts[i]["Name"] == contact_to_delete.capitalize():
            #If the name is found, remove the outter dictionary entirely, then exit this loop to mitigate errors
            contacts.pop(i)
            break

#Function for searching contacts by name
def Search_Contact():
    contact_found = False
    #Request the user provide a name for the contact they want information on
    contact_to_search = input("What is the name of the contact you would like to search? ")
    #Remove any extra spaces
    contact_to_search = contact_to_search.strip()
    #Iterate through the nested dictionaries, checking for a matching name value
    for i in contacts:
        if contacts[i]["Name"] == contact_to_search.capitalize():
            #When a matching name is found, provide the information of the listed contact
            print(f"Name: {contacts[i]["Name"]}, Phone Number: {contacts[i]["Phone Number"]}, Email: {contacts[i]["Email"]}, Address: {contacts[i]["Address"]}")
            #Ensure feedback of an unsuccessful search is not triggered and break out of the loop
            contact_found = True
            break
    #If a matching name is not found, provide the user with feedback
    if contact_found == False:
        print("A contact with that name was not found.")

#Function for displaying contacts
def Display_Contacts():
    for i in contacts:
        print(f"Name: {contacts[i]["Name"]}, Phone Number: {contacts[i]["Phone Number"]}, Email: {contacts[i]["Email"]}, Address: {contacts[i]["Address"]}")

#Function for exporting contacts to a text file
def Export_Contacts():
    #Open a new/existing file to write to using a with statement so the file closes after writing is complete
    with open("export_contacts.txt", "w") as file:
        #Iterate through each contact in the outer dictionary
        for i in contacts:
            #Iterate through the contact information in the nested dictionary
            for j in contacts[i]:
                current_contact_info = re.sub("\s", "_", contacts[i][j])
                #Write the value of each key to the text file
                file.write(f"{current_contact_info} ")
            #Separate each outer dictionary with a new line
            file.write(f"\n")

    #Provide feedback for the user so they know their contacts were exported successfully 
    print("Your contacts have been exported.")

#Function for importing contacts from a text file
def Import_Contacts():
    #Request the user provide a valid text file for importing contacts, one has been provided that is formatting for this code
    import_contacts = input("Please enter the file you wish to import contacts from (example: textfile.txt): ")
    valid_text_file = re.search(r"\b[A-Za-z0-9._%+-]+\.txt$\b", import_contacts)

    #If the provided file is valid, open the specified file as read only
    if valid_text_file != None:
        #Check to see if the user provided text file can be found
        try:
            contacts_file = open(import_contacts, "r")

            #Iterate through each line of the text file, split the line of string into a list 
            for line in contacts_file:
                contact_info = line.split()
                #Assign each segment of the list in a specific format, replacing _underscores_ with spaces
                contact_name = re.sub("_", " ", contact_info[0])
                contact_number = re.sub("_", " ", contact_info[1])
                contact_email = re.sub("_", " ", contact_info[2])
                contact_address = re.sub("_", " ", contact_info[3])

                #Add the new contact information from the list to the nested dictionary of contacts
                new_contact_info = {"Name": contact_name, "Phone Number": contact_number, "Email": contact_email, "Address": contact_address}
                contacts.update({contact_number: new_contact_info})

            #Close the file after everything is resolved
            contacts_file.close()

            #Provide feedback for the user so they know their contacts were imported successfully 
            print("Your contacts have been imported.")

        except FileNotFoundError:
            print("I'm sorry, the text file provided could not be found. Returning to main menu..")

    #If the user input is not a valid text file, provide feedback and return to the main menu
    elif valid_text_file == None:
        print("I'm sorry, that is not a valid text file. Returning to main menu..")

def Display_Options():
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Display options again")
    print("9. Quit")

#Welcome the user and display a list of option for the user to choose from
print("Welcome to the Contact Management System!")
print("Menu:")
print("1. Add a new contact")
print("2. Edit an existing contact")
print("3. Delete a contact")
print("4. Search for a contact")
print("5. Display all contacts")
print("6. Export contacts to a text file")
print("7. Import contacts from a text file")
print("8. Display options again")
print("9. Quit")

#Request user input for selecting menu options, display message if the user does not input a numbered item
try:
    user_input = int(input("Please enter your selection: "))

#If the user does not provide appropriate input, use a default value to iterate back through the loop for another prompt
except ValueError:
    print("Please enter one of the numbered selections listed.")
    user_input = 0

#Use a while loop to call functions corresponding to which selection the user made 
while user_input != 9:
    if user_input == 1:
        Add_Contact()
    elif user_input == 2:
        Edit_Contact()
    elif user_input == 3:
        Delete_Contact()
    elif user_input == 4:
        Search_Contact()
    elif user_input == 5:
        Display_Contacts()
    elif user_input == 6:
        Export_Contacts()
    elif user_input == 7:
        Import_Contacts()
    elif user_input == 8:
        Display_Options()
    elif user_input == 9:
        break
    else:
        user_input = 0
    
    #Secondary prompt to request user input after selections have been made, until they quit the app
    try:
        user_input = int(input("Please enter your selection: "))
    except ValueError:
        print("Please enter one of the numbered selections listed.")
        user_input = 0

#Thank the user for using the contact management system upon exiting the loop
print("Thank you for using the Contact Management System! Good-bye!")