Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact}")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if found_contacts:
            print("\nFound Contacts:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found with that name.")

    def update_contact(self, index, phone=None, email=None):
        try:
            contact = self.contacts[index]
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            print(f"Contact '{contact.name}' updated successfully.")
        except IndexError:
            print("Invalid contact number.")

    def delete_contact(self, index):
        try:
            removed_contact = self.contacts.pop(index)
            print(f"Contact '{removed_contact.name}' deleted successfully.")
        except IndexError:
            print("Invalid contact number.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
...         print("5. Delete a contact")
...         print("6. Exit")
... 
...         choice = input("Enter your choice (1-6): ")
... 
...         if choice == "1":
...             name = input("Enter contact name: ")
...             phone = input("Enter contact phone: ")
...             email = input("Enter contact email: ")
...             contact_book.add_contact(name, phone, email)
...         elif choice == "2":
...             contact_book.view_contacts()
...         elif choice == "3":
...             name = input("Enter the name to search for: ")
...             contact_book.search_contact(name)
...         elif choice == "4":
...             contact_book.view_contacts()
...             try:
...                 index = int(input("Enter the contact number to update: ")) - 1
...                 phone = input("Enter new phone (leave blank to keep current): ")
...                 email = input("Enter new email (leave blank to keep current): ")
...                 contact_book.update_contact(index, phone if phone else None, email if email else None)
...             except ValueError:
...                 print("Please enter a valid number.")
...         elif choice == "5":
...             contact_book.view_contacts()
...             try:
...                 index = int(input("Enter the contact number to delete: ")) - 1
...                 contact_book.delete_contact(index)
...             except ValueError:
...                 print("Please enter a valid number.")
...         elif choice == "6":
...             print("Exiting the program...")
...             break
...         else:
...             print("Invalid choice. Please try again.")
... 
... if __name__ == "__main__":
