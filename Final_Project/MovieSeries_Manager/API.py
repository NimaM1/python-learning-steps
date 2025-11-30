import requests
import storage
import colorama

API_key = "&apikey=8be8c8e7"
base_url = "http://www.omdbapi.com/?"


def pro_Search():
    while True:
        try:
            type = input(colorama.Fore.LIGHTBLUE_EX +
                         "Are you looking for a Movie or a Series? ").strip().title()
            if type == "Movie" or type == "Series":
                title = input(colorama.Fore.LIGHTBLUE_EX +
                              f"Enter the {type} title you are looking for: ").strip().lower()
                break
            else:
                print(colorama.Fore.RED + "Please choose Movie or Series!!")
                continue
        except ValueError:
            print(colorama.Fore.RED + "Please choose a Valid option!!")

    # API info
    url = f"{base_url}s={title}&type={type}{API_key}"
    response = requests.get(url)
    data = response.json()
    try:
        movies = data["Search"][:5]
    except KeyError:
        print(colorama.Fore.RED + f"There are No search results for {title}")
        return

    for index, item in enumerate(movies, 1):
        title = item.get("Title")
        poster = item.get("Poster")
        print(colorama.Fore.WHITE +
              f"result ({index}) '{title}', {type} Poster : {poster}")
    while True:
        try:
            user_choice = int(
                input(colorama.Fore.LIGHTBLUE_EX + "\nEnter the search number: "))
            selected = movies[user_choice - 1]
            break
        except (ValueError, IndexError):
            print(colorama.Fore.RED + "Invalid selection!")

    title = selected["Title"]
    select_url = f"{base_url}t={title}{API_key}"
    selectresponse = requests.get(select_url)
    selectdata = selectresponse.json()

    ratings = selectdata.get("Ratings", [])
    imdb_rating = None
    rotten_rating = None
    for rate in ratings:
        source = rate.get("Source")
        value = rate.get("Value")

        if source == "Internet Movie Database":
            imdb_rating = value
        elif source == "Rotten Tomatoes":
            rotten_rating = value

    moviedata = {'released': selectdata.get("Released"), 'genre': selectdata.get("Genre"), 'diractor': selectdata.get("Director"),
                 'writer': selectdata.get("Writer"), 'actor': selectdata.get("Actors"), 'plot': selectdata.get("Plot"),
                 'country': selectdata.get("Country"), 'poster': selectdata.get("Poster")}
    if moviedata['released'] == "N/A":
        moviedata['released'] = "No Data"
    if moviedata['diractor'] == None:
        moviedata['diractor'] = "No Data"

    print(colorama.Fore.YELLOW +
          f"\n'{title}' Directed by {moviedata['diractor']} Released at {moviedata['released']} ")
    print(colorama.Fore.YELLOW +
          f"Writer : {moviedata['writer']}\n Actor : {moviedata['actor']}")
    print(colorama.Fore.YELLOW +
          f"Genre : {moviedata['genre']}\n Description : {moviedata['plot']}")
    print(colorama.Fore.YELLOW +
          f"Ratings:\n [ IMDB ] : '{imdb_rating}' , [ Rotten Tomatoes ] : '{rotten_rating}' ")
    print(colorama.Fore.YELLOW + f"Producer Country : {moviedata['country']}")

    storage.save_List(
        title, moviedata['poster'], moviedata['released'], moviedata['genre'], imdb_rating, rotten_rating)

    storage.history(title, moviedata.get('diractor'), moviedata.get('poster'))
