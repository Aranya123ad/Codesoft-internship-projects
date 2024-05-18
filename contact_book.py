class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'address': address}
        print(f"Contact for {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts.values():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts.values() if search_term in contact['name'] or search_term in contact['phone']]
        if not results:
            print(f"No contacts found for search term: {search_term}")
            return
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, phone, name=None, email=None, address=None):
        if phone in self.contacts:
            if name:
                self.contacts[phone]['name'] = name
            if email:
                self.contacts[phone]['email'] = email
            if address:
                self.contacts[phone]['address'] = address
            print(f"Contact for {phone} updated.")
        else:
            print("Contact not found.")

    def delete_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            print(f"Contact for {phone} deleted.")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
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
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            phone = input("Enter the phone number of the contact to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(phone, name=name if name else None, email=email if email else None, address=address if address else None)
        elif choice == '5':
            phone = input("Enter the phone number of the contact to delete: ")
            contact_book.delete_contact(phone)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
