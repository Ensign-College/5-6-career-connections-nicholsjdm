import requests
import json

def get_ch_summary(book, summary):
  base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

  # User input URL using variables below
  url = f"{base_url}{book}/chapter}"

  # Call API
  response = requests.get(url)
  
  # Retrieve chapter summary and return the value
  data = response.json()
  summary = data['chapters'][0]['summary']
  return summary
  
def main():
  # Greeting and ask user for book and chapter
  print("Welcome to the Book of Mormon Summary Tool!")

  # Create a while loop for multiple entries
  while True:
    # Ask for user input
    book = input("Select a book from the Book of Mormon: ").replace(" ", "-").lower() # Replace spaces with hyphens and convert to lowercase
    chapter = input("Select a chapter from the book you selected: ")

    # Call the function above and assign it a variable
    summary = get_ch_summary(book, chapter)
    
    # Print Result
    print(f"Summary of {book.title()} chapter {chapter}:")
    print(summary)

    # Ask user if they want to repeat
    again = input("Would you like to view another (Y/N)? ").upper()
    if again != 'Y':
      print("Thank you for using the Book of Mormon Summary Tool!")
      break

main()
