import json
import os
from datetime import datetime
import analyzer
import colorama

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))

watchlistFile = os.path.join(DATA_DIR, "watch_List.json")
favorite = os.path.join(DATA_DIR, "favorite_list.json")
searchhisfile = os.path.join(DATA_DIR, "search_history.json")


def main():
    check_file()
    save_List()
    show_list()
    delete()


def check_file(myfile):
    if not os.path.exists(myfile) or os.stat(myfile).st_size == 0:
        with open(myfile, "w") as file:
            json.dump([], file, indent=4)


def save_List(title, poster, release, genre, imdb, tomato):
    addList = input(colorama.Fore.LIGHTBLUE_EX +
                    f"\nDo you want to add {title} to any of your lists? ").strip().lower()
    if "y" in addList:
        while True:
            which = input(colorama.Fore.LIGHTBLUE_EX +
                          f"\nDo you want to add {title} to your Watch List or Favorite List? ").strip().lower()
            if "watch" in which or "favorite" in which:
                break
            else:
                print(colorama.Fore.RED +
                      "Please choose 'Watch list' or 'Favorite list' !!")
                continue
    elif "n" in addList:
        print(colorama.Fore.YELLOW + "OK!!")

    if "watch" in which:
        myfile = watchlistFile
    elif "favorite" in which:
        myfile = favorite

    check_file(myfile)

    new_movie = {"title": title, "poster": poster,
                 "release": release, "genre": genre, "imdb": imdb, "tomato": tomato}
    with open(myfile, "r") as file:
        data = json.load(file)

    for line in data:
        if line['title'].lower() == new_movie['title'].lower():
            print(colorama.Fore.RED +
                  f"You have already added {new_movie['title']} to your list. ")
            return

    data.append(new_movie)
    with open(myfile, "w") as file:
        json.dump(data, file, indent=4)
    print(colorama.Fore.YELLOW + f"You have added {title} to your list.")


def show_list():
    while True:
        try:
            which = input(colorama.Fore.LIGHTBLUE_EX +
                          "Do you want to see your Watch list or your Favorite list? ").strip().lower()
            if "watch" in which or "favorite" in which:
                break
            else:
                print(colorama.Fore.RED +
                      "Please choose your Watch list or Favorite list!!")
        except ValueError:
            print(colorama.Fore.RED +
                  "Please choose your Watch list or Favorite list!!")
    if "watch" in which:
        myfile = watchlistFile
    elif "favorite" in which:
        myfile = favorite

    with open(myfile, "r") as file:
        data = json.load(file)

    if os.stat(myfile).st_size == 0 or data == []:
        print(colorama.Fore.RED + "You have no saved Movie/Series in your list.")
        return

    with open(myfile, "r") as file:
        data = json.load(file)

    print(colorama.Fore.YELLOW + "Here is your list:")
    for index, line in enumerate(data, 1):
        print(colorama.Fore.WHITE + f"({index}) {line['title']}")
        print(colorama.Fore.WHITE +
              f"Genre : {line['genre']}, IMDB : {line['imdb']}\n")

    analyzer.genrezer(myfile)
    analyzer.imdbezer(myfile)

    filter_list = input(colorama.Fore.LIGHTBLUE_EX +
                        "\nDo you want to filter your List? ").strip().lower()
    if "y" in filter_list:
        filterList(myfile)
    elif "n" in filter_list:
        print(colorama.Fore.YELLOW + "OK!")


date_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def history(title, director, poster):
    check_file(searchhisfile)
    new_search = {'title': title, 'director': director,
                  'poster': poster, 'date': date_time}

    with open(searchhisfile, "r") as file:
        data = json.load(file)

    data.append(new_search)
    with open(searchhisfile, "w") as file:
        json.dump(data, file, indent=4)


def delete():
    while True:
        which = input(colorama.Fore.LIGHTBLUE_EX +
                      "Enter the list name (Watch list \ Favorite List): ").strip().lower()
        if "watch" in which or "favorite" in which:
            break
        else:
            print(colorama.Fore.RED + "Please choose Watch list or Favorite list!!")

    if "watch" in which:
        myfile = watchlistFile
    elif "favorite" in which:
        myfile = favorite

    item = input(colorama.Fore.LIGHTBLUE_EX +
                 "Enter the Movie Title you want to Delete: ").strip().lower()

    check_file(myfile)

    with open(myfile, "r") as file:
        data = json.load(file)

    new_data = [line for line in data if line["title"].strip().lower()
                != item]
    if len(new_data) > len(data):
        print(colorama.Fore.YELLOW +
              f"{item.title()} has been successfully deleted out of List")
    else:
        print(colorama.Fore.RED +
              f"There is no match title for '{item}' in your List.")

    with open(myfile, "w") as file:
        json.dump(new_data, file, indent=4)


def filterList(myfile):
    while True:
        filter_by = input(colorama.Fore.LIGHTBLUE_EX +
                          "Please choose by 'Genre' or 'IMDB' : ").strip().lower()
        if "genre" in filter_by or "imdb" in filter_by:
            break
        else:
            print(colorama.Fore.RED + "Please choose by 'Genre' or 'IMDB' !!!")
            continue
    with open(myfile, "r") as file:
        data = json.load(file)

    if "genre" in filter_by:
        genre = input(colorama.Fore.LIGHTBLUE_EX +
                      "which Genre you want to filter your list by? ")

        found = False
        for line in data:
            if genre in line['genre']:
                found = True
                print(colorama.Fore.YELLOW +
                      f"{line['title']} by {line['genre']}")
                print(colorama.Fore.YELLOW +
                      f"Ratings : IMDB '{line['imdb']}', Rotten Tomato '{line['tomato']}'")
        if not found:
            print(colorama.Fore.RED +
                  f"You have no save Movie/Series with {genre} genre in your list.")

    elif "imdb" in filter_by:
        while True:
            try:
                imdb = float(colorama.Fore.LIGHTBLUE_EX +
                             input("Enter the minimum IMDB rating you want(0/10): "))
                break
            except ValueError:
                print(colorama.Fore.RED + "Please Enter a valid IMDB Rate!!")
                continue
        found = False
        for line in data:
            imdb_raw = line.get("imdb", "0/10")
            try:
                real_imdb = float(imdb_raw.split("/")[0])
                if real_imdb >= imdb:
                    found = True
                    print(colorama.Fore.YELLOW +
                          f"\n{line['title']} (IMDB: {real_imdb}/10)")
                    print(colorama.Fore.YELLOW +
                          f"Genre: {line['genre']} - Rotten Tomato: {line['tomato']}")
            except (ValueError, IndexError):
                continue
        if not found:
            print(colorama.Fore.RED +
                  f"\nNo movie/series found with IMDB rating more than {imdb}!!")


if __name__ == "__main__":
    main()
