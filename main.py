def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    character_list = chars_to_sorted_list(character_count)
    print_report(path, word_count, character_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
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

def chars_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(path, word_count, character_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} found in the document\n")
    for item in character_list:
        print(f"The {item["char"]} character was found {item["num"]} times")
    print("--- End report ---")

main()