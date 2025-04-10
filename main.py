from stats import count_words
from stats import character_dictionary_list

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    sorted_character_list = character_dictionary_list(text)
    print(
        "=" * 12 + " BOOKBOT " + "=" * 12 + 
        "\nAnalyzing book found at books/frankenstein.txt..." +
        "\n" + "-" * 11 + " Word Count " + "-" *10 +
        "\n" f"Found {word_count} total words" +
        "\n" + "-" * 8 + " Character Count " + "-" * 8)
    create_character_print(sorted_character_list)
    print("=" * 14 + "END" + "=" * 14)


# prints out characters and their values

def create_character_print (sorted_character_list):
    for character in sorted_character_list:
        if character["letter"].isalpha():
            print(f"{character["letter"]}: {character["count"]}")

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

main()