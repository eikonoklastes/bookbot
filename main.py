import sys
from stats import *   # Import the count_words function from stats module

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def main():
    # check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]  # Get the book path from command line argument
    book_text = get_book_text(book_path)  # Get the book text   
    num_words = count_words(book_text)  # Count the words in the book
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")  # Print the word count
    print("--------- Character Count -------")

    unique_chars = count_characters(book_text)  # Count the unique characters
    book_report(num_words, unique_chars)  # Generate the book report

main()