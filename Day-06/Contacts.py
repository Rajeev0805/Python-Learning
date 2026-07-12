contacts = {}
def add_contact():
    name = input("Enter the Name of the Student")
    phn = input("Enter Student Mobile Number")
    contacts[phn] = name
    print(f"Contact for {name} saved successfully.")
def search_contact():
    phn = input("Enter the mobile number to search the contact: ")
    if phn in contacts: 
        print(f"Name: {contacts[phn]}")
    else:
        print("Contact not found.")
def update_contact():
    phn = input("Enter the Mobile Number you want to update")
    if phn in contacts:
        new_name = input("Enter the New Name: ")
        contacts[phn] = new_name
        print("Contact updated successfully.")
    else:
        print("Contact not found.")
def delete_contact():
    phn = input("Enter the Mobile Number you want to delete")
    if phn in contacts:
        deleted_name = contacts.pop(phn)
        print(f"Contact '{deleted_name}' deleted successfully.")
        print("Contact deleted successfully.")
    else:
        print("Contact Not Found.")
def display_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("===== CONTACT LIST =====")
    print()
    print(f"{'Phone Number':<16}Name")
    print("-" * 25)

    for phone, name in contacts.items():
        print(f"{phone:<16}{name}")

while True:

    print("1.Create/Add Contact \n2.Search Contact\n3.Update Contact\n4.Delete Contact\n5.Display Contacts\n6.Exit")

    choice = input()

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        display_contacts(contacts)

    elif choice == "6":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid Choice.")

