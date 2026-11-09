
contacts = []

def add_contact():
    try:
        name = input("enter contact name: ").strip()
    except ValueError:
        print("Invalid input for contact name.")
        return

    try:
        phone = input("enter contact phone number: ").strip()
    except ValueError:
        print("Invalid input for phone number.")
        return

    try:
        email = input("enter contact email: ").strip()
    except ValueError:
        print("Invalid input for email.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
        })
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        
        for number, contact in enumerate(contacts, start=1):
            print(f"{number}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    search_name = input("Enter contact name to search: ").strip()

    if not search_name:
        print("Please enter a name.")
        return

    found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]

    if found_contacts:
        for number, contact in enumerate(found_contacts, start=1):
            print(f"{number}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("Contact not found.")
        

def update_contact():
    search_name = input("enter contact name to update: ").strip()

    if not search_name:
        print("Please enter a name.")
        return

    found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]

    if found_contacts:
        for number, contact in enumerate(found_contacts, start=1):
            print(f"{number}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

        choice = input("Enter the number of the contact to update: ").strip()

    else:
        print("Contact not found.")
        return
        
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            selected_contact = found_contacts[int(choice) - 1]
            new_name = input(f"Enter new name (leave blank to keep '{selected_contact['name']}'): ").strip()
            new_phone = input(f"Enter new phone (leave blank to keep '{selected_contact['phone']}'): ").strip()
            new_email = input(f"Enter new email (leave blank to keep '{selected_contact['email']}'): ").strip()

            if new_name:
                selected_contact['name'] = new_name
            if new_phone:
                selected_contact['phone'] = new_phone
            if new_email:
                selected_contact['email'] = new_email

            print("Contact updated successfully!")
        else:
            print("Invalid selection.")    
                
         
def delete_contact():
    search_name = input("Enter contact name to delete: ").strip()

    if not search_name:
        print("Please enter a name.")
        return

    found_contacts = [contact for contact in contacts if search_name.lower() in contact['name'].lower()]

    if found_contacts:
        for number, contact in enumerate(found_contacts, start=1):
            print(f"{number}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

        choice = input("Enter the number of the contact to delete: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            selected_contact = found_contacts[int(choice) - 1]
            contacts.remove(selected_contact)
            print("Contact deleted successfully!")
        else:
            print("Invalid selection.")
    else:
        print("Contact not found.")
    
while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
           
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()    
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("invalid choice")