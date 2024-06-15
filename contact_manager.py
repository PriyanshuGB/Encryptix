# contact_manager.py

import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                self.display_contact(contact)

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def display_contact(self, contact):
        print(f"\nName: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}\n")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            manager.update_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
