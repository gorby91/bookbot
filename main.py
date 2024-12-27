def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    print(f"There are {count_words(file_contents)} in the document")
    character_count = count_characters(file_contents)
    character_list = list_dict(character_count)
    print_char_report(character_list)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    character_count = {}
    for char in file_contents.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def list_dict(dict):
    char_list = []
    for char in dict:
        if char.isalpha():
            char_list.append({"char": char, "num": dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def print_char_report(character_list):
    for item in character_list:
        print(f"The {item["char"]} character was found {item["num"]} times")

main()