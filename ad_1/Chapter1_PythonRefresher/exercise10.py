# this program stores details about a film using a dictionary
# it then loops through the dictionary to print all the key-value pairs

film = {
    "title": "inception",
    "director": "christopher nolan",
    "year": 2010,
    "genre": "sci-fi"
}

print("film details:")
for key, value in film.items():
    print(f"{key}: {value}")
