import requests
import os
import json
from datetime import datetime
import colorama


print(colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX + """
_______________________________________________________________________
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                  <<<< Online Library Manager >>>>
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
_______________________________________________________________________

[1] Searching Book by Title and Borrowing
[2] Searching Author Info
[3] Borrowed Book List
[4] Return Book
[5] Exit The Program


""")


def main():
    while True:
        while True:
            try:
                option = int(input(colorama.Fore.WHITE + "\n>>>>> "))
                if 1 <= option <= 5:
                    break
                else:
                    print(colorama.Fore.RED +
                          "Please enter a valid number of the menu!!!")
                    continue
            except ValueError:
                print(colorama.Fore.RED +
                      "Please enter a valid number of the menu!!!")

        if option == 1:
            getBook_title()
        elif option == 2:
            get_author()
        elif option == 3:
            save_file = "borrow.json"
            borrow_List(save_file)
        elif option == 4:
            return_book()
        elif option == 5:
            print(colorama.Fore.LIGHTYELLOW_EX + "Have a nice day :) ")
            break


def getBook_title():
    # API info

    title = input(colorama.Fore.WHITE +
                  "\nEnter the book title: ").strip().title()
    url_title = title.replace(" ", "+")
    url = f"https://openlibrary.org/search.json?q={url_title}"
    response = requests.get(url)
    data = response.json()

    books = data["docs"][:10]
    for index, item in enumerate(books, 1):
        book_title = item["title"]
        authors = item["author_name"]
        print(colorama.Fore.LIGHTBLUE_EX +
              f"Search {index} : {book_title} by {authors}")

    while True:
        try:
            user_choice = int(input(colorama.Fore.WHITE +
                              "\nEnter the search number: "))
            if 1 <= user_choice <= 10:
                break
            else:
                print(colorama.Fore.RED +
                      "Please enter a valid number of the 10 search numbers!!")
                continue
        except ValueError:
            print(colorama.Fore.RED +
                  "Please enter a valid number of the 10 search numbers!!")
    selected_book = books[user_choice - 1]

    book_title = selected_book["title"]
    authors = selected_book["author_name"]

    publish_year = selected_book.get("first_publish_year")
    if not publish_year:
        publish_year = "There is no first publish year!"

    print(colorama.Fore.CYAN + f"\n>>{book_title}<< by {authors}")
    print(colorama.Fore.CYAN + f"First published in > {publish_year}")

    save_file = "onlineLibrary_searchHistory.json"
    save_search(save_file, book_title, authors)

    borrow = input(colorama.Fore.WHITE +
                   f"\nDo you want to borrow {book_title}? ").strip().lower()
    if "y" in borrow:
        print(colorama.Fore.YELLOW + f"You have borrowed {book_title}")
        save_file = "borrow.json"
        save_search(save_file, book_title, authors)
    elif "n" in borrow:
        print(colorama.Fore.YELLOW + "OK")


date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def save_search(save_file, book, author):

    if not os.path.exists(f"{save_file}") or os.stat(f"{save_file}").st_size == 0:
        with open(f"{save_file}", "w") as file:
            json.dump([], file, indent=4)

    newSearch = {"book": book, "author": author, "date_time": date_time}
    with open(f"{save_file}", "r") as file:
        data = json.load(file)
    data.append(newSearch)
    with open(f"{save_file}", "w") as file:
        json.dump(data, file, indent=4)


def get_author():
    # API info
    author = input(colorama.Fore.WHITE +
                   "Enter the Author name you are looking for: ").strip().title()
    url_author = author.replace(" ", "+")
    url = f"https://openlibrary.org/search/authors.json?q={url_author}"
    response = requests.get(url)
    data = response.json()

    authors = data["docs"][:10]
    for index, item in enumerate(authors, 1):
        author_name = item["name"]
        print(f"search > {index}, Author name : {author_name}")

    while True:
        try:
            user_choice = int(
                input(colorama.Fore.WHITE + "\nEnter the search number you are looking for: "))
            if 1 <= user_choice <= 10:
                break
            else:
                print(colorama.Fore.RED +
                      "Please enter a valid number of the 10 search numbers!!")
        except ValueError:
            print(colorama.Fore.RED +
                  "Please enter a valid number of the 10 search numbers!!")

    selected_author = authors[user_choice - 1]
    author_name = selected_author.get("name")
    author_birth = selected_author.get("birth_date")
    if not author_birth:
        author_birth = f"There is not any data about {author_name} birthday"
    top_book = selected_author["top_work"]
    subject = selected_author.get("top_subjects")
    if not subject:
        subject = "None"
    author_key = selected_author["key"]
    print(colorama.Fore.LIGHTGREEN_EX +
          f">>{author_name}<< born in {author_birth}")
    print(colorama.Fore.LIGHTGREEN_EX + f"author's top books : {top_book}")
    print(colorama.Fore.LIGHTGREEN_EX + f"author's top book subjects : ")
    print(colorama.Fore.LIGHTGREEN_EX +
          f"{subject[0]}, {subject[1]}, {subject[2]}")

    workurl = f"https://openlibrary.org/authors/{author_key}/works.json"
    response = requests.get(workurl)
    work_data = response.json()

    print(colorama.Fore.LIGHTBLUE_EX +
          f"\nBooks by {selected_author['name']}:\n")
    for i, work in enumerate(work_data["entries"][:10], 1):
        print(colorama.Fore.LIGHTBLUE_EX + f"{i}. {work['title']}")

    save_file = "onlineLibrary_searchHistory.json"
    save_search(save_file, top_book, author_name)


def borrow_List(save_file):
    if not os.path.exists(f"{save_file}") or os.stat(f"{save_file}").st_size == 0:
        with open(f"{save_file}", "w")as file:
            json.dump([], file, indent=4)
        print(colorama.Fore.YELLOW + "You have no borrowed book")
        return
    with open(f"{save_file}", "r")as file:
        data = json.load(file)
    print(colorama.Fore.YELLOW + "Here are you'r borrowd books: \n")
    for line in data:
        title = line.get('book', 'Unknown Title')
        author = line.get('author', 'Unknown Author')
        print(colorama.Fore.YELLOW + f"{title} by {author}")


def return_book():
    returnbook = input(colorama.Fore.WHITE +
                       "Which book do you want to return? ").strip().lower()

    with open("borrow.json", "r") as file:
        data = json.load(file)

    newdata = [line for line in data if line["book"].strip().lower()
               != returnbook]

    if len(newdata) < len(data):
        print(colorama.Fore.YELLOW +
              f"'{returnbook.title()}' has been successfully returned.")
    else:
        print(colorama.Fore.YELLOW +
              f"No borrowed book matched the title '{returnbook.title()}'.")

    with open("borrow.json", "w") as file:
        json.dump(newdata, file, indent=4)


main()
