import json
import sys

# Define file name for persistent storage
CONTACTS_FILE = "contacts.json"

# Function to load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Load contacts initially
contacts = load_contacts()

# Function to display menu
def display_menu():
    print("\n*** Contact Management System ***")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Modify Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    print("\nContact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return
    print("\n*** Contact List ***")
    for i, contact in enumerate(contacts, start=1):
        print(f"Contact {i}:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}\n")

# Function to search for a contact
def search_contact():
    search_name = input("\nEnter the name to search: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            print("\nContact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print("\nContact not found.")

# Function to modify a contact
def modify_contact():
    modify_name = input("\nEnter the name of the contact to modify: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == modify_name:
            contact['name'] = input("Enter new name: ").strip()
            contact['phone'] = input("Enter new phone number: ").strip()
            contact['email'] = input("Enter new email: ").strip()
            save_contacts()
            print("\nContact modified successfully!")
            return
    print("\nContact not found.")

# Function to delete a contact
def delete_contact():
    delete_name = input("\nEnter the name of the contact to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == delete_name:
            del contacts[i]
            save_contacts()
            print("\nContact deleted successfully!")
            return
    print("\nContact not found.")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            modify_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExiting...")
            sys.exit()
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
