import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

response = requests.get(base_url)
data = response.json()

# Greeting and user input
print("This program will display a chapter summary from anywhere in the Book of Mormon!")
book = input("Select a book from the Book of Mormon: ")
chapter = input("Select a chapter from the book you selected: ")

# We need to find a way to match the value with a zero-index list within a dictionary

# This will access each book
print(data['books']['title'][USER INPUT HERE])

# This will access each chapter of the selected book and print the summary
print(data[...
