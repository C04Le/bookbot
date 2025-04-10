from stats import count_words
from stats import count_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    characters = count_characters(text)
    print(f"{word_count} words found in the document")
    print(characters)

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

main()