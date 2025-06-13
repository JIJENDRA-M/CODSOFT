contacts = []
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
def search_contact():
    query = input("Search by name or phone: ").lower()
    found = False
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True
            break
    if not found:
        print("No contact matched your search.")
def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave field blank to keep the current value.")
            new_phone = input(f"New phone (current: {contact['phone']}): ")
            new_email = input(f"New email (current: {contact['email']}): ")
            new_address = input(f"New address (current: {contact['address']}): ")

            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("Contact updated.")
            return
    print("Contact not found.")
def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
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
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
