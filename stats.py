def count_words(text):
    count = len(text.split())
    return count

def count_characters(text):
    character_dictionary = {}
    text_characters = list(text.lower())

    for character in text_characters:
        if character not in character_dictionary:
            character_dictionary[character] = 1
        elif character in character_dictionary:
            character_dictionary[character] += 1
    
    return character_dictionary
