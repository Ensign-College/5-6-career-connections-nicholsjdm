import requests
import json

def get_ch_summary(book, chapter):
  base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
  url = f"{base_url}{book}/chapter{chapter}"
  response = requests.get(url)

  # Check for errors for API request
  if response.status_code == 200:
    data = response.json()
    summary = data['chapters']['summary']
    return summary
  else:
      print("Error")
      return None
  
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
    
    # Check for error and display results
    if summary:
      print(f"Summary of {book.title()} chapter {chapter}:")
      print(summary)
    else:
      print("No summary available.")

    # Ask user if they want to repeat
    again = input("Would you like to view another (Y/N)? ").upper()
    if again != 'Y':
      print("Thank you for using the Book of Mormon Summary Tool!")
      break

main()
