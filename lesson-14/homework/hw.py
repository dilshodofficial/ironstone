import json

json_str = '{"name": "Alice", "age": 30, "is_student": false}'

data = json.loads(json_str)
print(data["name"])  

json_back = json.dumps(data, indent=2)
print(json_back)
import json
json_str = '{"name": "Alice", "age": 30, "is_student": false}'
data = json.loads(json_str)
print(data["name"])

json_back = json.dumps(data, indent=2)
print(json_back)
import json
json_str = '{"name": "Alice", "age": 30, "is_student": false}'
data = json.loads(json_str)
print(data["age"])

json_b = json.dumps(data, indent=2)
print(json_b)
import json
data = {"name": "Alice", "age": 30}

with open("smth.json", "w") as f:
  json.dump(data, f)
import json

with open("students.json") as file:
  students = json.load(file)

for student in students:
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")
    print("-" * 20)
weather

import requests

def get_weather(city_name):
    api_key = "YOUR_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"🌤 Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("❌ Failed to retrieve weather data. Check your city name or API key.")

# Вызов функции
get_weather("Tashkent")

import json
import os

FILE_NAME = "books.json"

def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")

    books = load_books()
    books.append({
        "title": title,
        "author": author,
        "year": int(year)
    })
    save_books(books)
    print("✅ Book added successfully!")

def update_book():
    title = input("Enter the title of the book to update: ")
    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            new_author = input(f"Enter new author (current: {book['author']}): ") or book["author"]
            new_year = input(f"Enter new year (current: {book['year']}): ") or book["year"]
            book["author"] = new_author
            book["year"] = int(new_year)
            save_books(books)
            print("✏️ Book updated successfully!")
            return
    print("❌ Book not found.")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    books = load_books()
    books = [book for book in books if book["title"].lower() != title.lower()]
    save_books(books)
    print("🗑️ Book deleted (if it existed).")

def main():
    while True:
        print("\n--- Book Manager ---")
        print("1. Add book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()

import requests
import random

API_KEY = "41805f06"  # Replace with your OMDb API Key

# Sample movies categorized by genre
genre_movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "The Dark Knight", "Gladiator"],
    "comedy": ["The Mask", "Superbad", "The Grand Budapest Hotel", "Step Brothers"],
    "drama": ["Forrest Gump", "The Shawshank Redemption", "The Godfather", "Fight Club"],
    "romance": ["Pride and Prejudice", "The Notebook", "La La Land", "Titanic"],
    "sci-fi": ["Inception", "Interstellar", "The Matrix", "Arrival"],
    "horror": ["The Conjuring", "Get Out", "A Quiet Place", "Hereditary"]
}

def fetch_movie_info(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def recommend_movie_by_genre():
    genre = input("Enter a movie genre (e.g., Action, Drama, Comedy): ").lower()

    if genre not in genre_movies:
        print("❌ Sorry, that genre is not supported.")
        return

    title = random.choice(genre_movies[genre])
    movie = fetch_movie_info(title)

    if movie and movie.get("Response") == "True":
        print("\n🎬 Recommended Movie:")
        print(f"Title: {movie['Title']}")
        print(f"Year: {movie['Year']}")
        print(f"Genre: {movie['Genre']}")
        print(f"Plot: {movie['Plot']}")
    else:
        print("❌ Could not fetch movie information.")

# Run the recommender
recommend_movie_by_genre()

