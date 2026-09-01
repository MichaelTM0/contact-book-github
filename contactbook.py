# ------------------------------------------
# Contact Book
# Author: Michael Murchie
#
# Features:
# - Add Contacts
# - View Contacts
# - Search Contacts
# - Delete Contacts
#
# Version: 1.0
# ------------------------------------------
#start with empty dictonary
contact_book = {}


def add_contact(contact_book):
    name = input("Enter name here: ").strip().title()
 #check if name already exist , and if not get required personal info   
    if name in contact_book:
        print(f"{name} already exists.")
        return
    else:
        print(f"Hey nice to meet you! creating new contact for {name} now!")
        
        
        number = input("Please enter you number here: ").strip()
        city = input("Please enter the city you live in: ").strip().title()
        state = input("Please enter the state you live in: ").strip().upper()
        

#create the inner dictionary(for each persons information)
    contact = {
        "name": name,
        "number": number,
        "city": city,
        "state": state
    }
    #here we add and or update the contact book
    contact_book[name] = contact
    print(f"All done! {name} has been succesfully saved!\n")
    
def view_contact(contact_book):
    if not contact_book:
        print("No contact exists.")
        return
    for contact in contact_book.values():
        print(contact)
        
def search_contact(contact_book):
    person = input("Please enter the name of who your looking for: ").strip().lower()
    found = False
    for contact in contact_book.values():
        if contact["name"].lower() == person:
            print(contact)
            found = True
    if not found:
        print("No records at this time.")
            
def delete_contact(contact_book):
    if not contact_book:
        print("Contact book is empty!")
        return
    x = input("Enter the name of the contact you want to delete: ").strip().lower()
    found = False
    for name in list(contact_book.keys()):
        if name.lower() == x:
            del contact_book[name]
            print(f"{name} has been deleted.")
            found = True
            break
    if not found:    
        print("No contact found!")
            
def main(contact_book):
    print("\n" + "=" * 50)
    print("CONTACT BOOK")
    print("=" * 50)
    
    while True:
        print("1. Add contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("=" * 50)
        
        choice = input("Please enter a option(1-5): ").strip()
    
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contact(contact_book)
        elif choice == "3":
            search_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            print("Thanks for using the contact book! Goodbye!")
            break
        else:
            print("Please enter a valid option!")
        
main(contact_book)