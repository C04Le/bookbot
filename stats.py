def count_words(text):
    count = len(text.split())
    return count


# defines how to sort list of dictionaries
# sort based on the value of key 'count'

def sort_on(dict):
    return dict["count"]


# create a sorted list of dictionaries
# from a dictionary of all characters and their count
# 2 key-value pairs > letter and count

def character_dictionary_list(text):
    character_dict = count_characters(text)
    character_list = []

    for key in character_dict.keys():
        new_character_dict = {}
        new_character_dict["letter"] = key
        new_character_dict["count"] = character_dict[key]
        character_list.append(new_character_dict)
    
    character_list.sort(reverse=True, key=sort_on)
    return character_list


# create a dictionary of all characters in text and their count
# key = the character, value = count how many times it appears

def count_characters(text):
    character_dictionary = {}
    text_characters = list(text.lower())

    for character in text_characters:
        if character not in character_dictionary:
            character_dictionary[character] = 1
        elif character in character_dictionary:
            character_dictionary[character] += 1
    
    return character_dictionary
