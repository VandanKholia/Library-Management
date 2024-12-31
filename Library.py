import json;

FILENAME = "library.json"

def load_data():
    try:
        with open(FILENAME,"r") as file:
               return json.load(file) 
    except FileNotFoundError:
        return {"books": [], "borrowed_books": {}}
    
def save_data(data):
    with open(FILENAME,"w") as file:
        json.dump(data,file,indent=4)   

#Add new book
def add_book(data,title,author,id):
    data["books"].append({"title":title, "author":author, "id":id})
    save_data(data)
    print(f"{title} added successfully")

#Display available books
def list_books(data):
    if data["books"]:
        print("\nAvailable books:\n")
        for book in data["books"]:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ID: {book['id']}\n")

def remove_book(data,id):
    book_to_remove=None
    for book in data["books"]:
        if book['id']==id:
            book_to_remove=book
            break
    if book_to_remove:
        data["books"].remove(book_to_remove)
        save_data(data)
        print(f"\"{book_to_remove['title']}\" removed successfully")
    else:
        print("Book not found")

def search_book(data, keyword):
    result = []
    for book in data["books"]:
        if keyword.lower() in book['author'].lower() or keyword.lower() in book['title'].lower():
            result.append(book)
    if result:
        print("\nSearch Results:\n")
        for book in result:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ID: {book['id']}\n")
    else:
        print("No books found.")

        
def main():
    data = load_data()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove book")
        print("3. Search books")
        print("4. List books")
        print("5. Exit")

        choice = input("\nEnter choice: ")
    
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            id = input("Enter book id: ")
            add_book(data,title,author,id)
        elif choice=="2":
            id = input("Enter book id: ")
            remove_book(data,id)
        elif choice=="3":
            keyword=input("Enter keyword to search: ")
            search_book(data,keyword)  
        elif choice=="4":
            list_books(data)
        elif choice=="5":
            print("Goodbye!!")
            break
    
if __name__ == "__main__":
    main()