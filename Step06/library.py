import json
import os

print("""
------------------------------------------------------------------
------------------------------------------------------------------
        **Hello and welcome to your personal library**
------------------------------------------------------------------
------------------------------------------------------------------
Please enter any number you would like to change in your library
[1] Add a new book with details: title, author, year, read_status.
[2] view all books in the library.
[3] Update the read status of a book.
[4] Search for books by title or author.
[5] Delete a book.
[6] Exit the program.""")


def main():
    while True:
        try:
            option = int(input(">>>>> "))
        except ValueError:
            print("Please enter a valid number. ")
            continue
        if option == 1:
            addBook()
        elif option == 2:
            view()
        elif option == 3:
            status()
        elif option == 4:
            search()
        elif option == 5:
            delete()
        elif option == 6:
            answer = input(
                "Are you sure you want to exit the program? ").strip().lower()
            if "y" in answer:
                print("Have a nice day then!!! ")
                break
            elif "n" in answer:
                continue


def addBook():
    if not os.path.exists("library.json") or os.stat("library.json").st_size == 0:
        with open("library.json", "w") as file:
            json.dump([], file, indent=4)
    library = []
    bookName = input(
        "Enter the name of the book you want to add: ").strip().title()
    author = input("Enter the name of it's author: ").strip().title()
    year = int(input("Enter the year that it's been published: "))
    readStatus = "not finished"
    new = {"title": bookName, "author": author,
           "year": year, "read status": readStatus}
    library.append(new)
    with open("library.json", "r") as file:
        data = json.load(file)
    data.append(new)
    with open("library.json", "w") as file:
        json.dump(data, file, indent=4)
    print(f"You have successfully added {bookName} to your library. ")


def view():
    with open("library.json", "r") as file:
        data = json.load(file)
    for line in data:
        print(
            f"{line['title']} by {line['author']} has been published in {line['year']}")


def status():
    status = input("Which book you want to mark as finished? ")
    with open("library.json", "r") as file:
        data = json.load(file)
    found = False
    for line in data:
        if line["title"] == status:
            line["read status"] = "finished"
            print(
                f"{line['title']} read status has been changed to finished")
            found = True
            break
    if not found:
        print("The book has not been found. ")
    with open("library.json", "w") as file:
        json.dump(data, file, indent=4)


def search():
    search = input(
        "Please enter the title of the book you want to know its info: ")
    found = False
    with open("library.json", "r") as file:
        data = json.load(file)
    for line in data:
        if line["title"] == search:
            print(
                f"""{line['title']} by {line['author']} has been published in {line['year']}
                  and its read status in your library is {line['read status']}""")
            found = True
    if not found:
        print(f"{search} has not been found!!! ")


def delete():
    delete = input("which book you would like to delete? ")
    with open("library.json", "r") as file:
        data = json.load(file)
    for i, line in enumerate(data):
        if line["title"] == delete:
            data.pop(i)
            print(f"You have deleted {delete}.")
    with open("library.json", "w") as file:
        json.dump(data, file, indent=4)


main()
