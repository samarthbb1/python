# 2a. Find All Occurrences of an Element
nums = [1, 2, 3, 2, 4, 2]
target = 2
indices = [i for i, x in enumerate(nums) if x == target]
print(f"Element {target} found at indices: {indices}")
OUTPUT:





# 2b. Library Book List (Add, Search, Display)
def add_book(library):
    """Adds a new book title and author to the dictionary."""
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    library[title] = author
    print(f"Book '{title}' added successfully!")

def search_book(library):
    """Searches for a book by its title."""
    title = input("Enter book title to search: ").strip()
    if title in library:
        print(f"Found: '{title}' by {library[title]}")
    else:
        print("Book not found in the library.")

def display_books(library):
    """Displays all books currently in the dictionary."""
    if not library:
        print("The library is currently empty.")
    else:
        print("\n--- Current Library List ---")
        for title, author in library.items():
            print(f"Title: {title} | Author: {author}")

def main():
    """Main function to handle user menu and choices."""
    library_data = {}
    
    while True:
        print("\n1. Add Book")
        print("2. Search Book")
        print("3. Display All Books")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_book(library_data)
        elif choice == '2':
            search_book(library_data)
        elif choice == '3':
            display_books(library_data)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

# Execute the program
if __name__ == "__main__":
    main()
