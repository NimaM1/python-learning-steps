Movie & Series Manager is a Python-based application that allows users to search, save, and manage their favorite movies and series using the OMDb API. The project demonstrates working with APIs, JSON storage, user interaction, and basic data analysis.

Features

Search Movie or Series:
Users can search for movies or series by title using the OMDb API and view details such as director, actors, plot, genre, release date, and ratings (IMDb & Rotten Tomatoes).

Save to Lists:
Users can add selected movies/series to Watch List or Favorite List, stored locally in JSON files.

Manage Lists:

View saved Watch List or Favorite List

Delete items from lists

Filter lists by Genre or Minimum IMDb Rating

Search History:
Keeps track of recent searches with date, title, director, and poster.

Data Analysis:
Provides insights into your lists:

Most common genres in your Watch/Favorite lists

Average IMDb rating of your saved movies/series

File Structure

main.py – Entry point of the program; handles the main menu and user input.

API.py – Handles movie/series search and fetches details from the OMDb API.

storage.py – Manages saving, deleting, and displaying lists, search history, and filtering options.

analyzer.py – Analyzes saved movies/series for common genres and average IMDb rating.

Requirements

Python 3.x

requests – For API calls

colorama – For colored terminal output

Install dependencies with:

pip install requests colorama

Usage

Run main.py to start the program.

Choose an option from the menu:

Search Movie/Series

Show Watch List / Favorite List

Delete an item

Exit

Follow prompts to search, save, and manage your movies/series.