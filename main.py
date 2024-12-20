def Main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_char_count(text)
    char_list = create_char_list(character_count)
    sorted_char_list = sorted(char_list, reverse=True, key=sort_dict)
    report = sorted_char_list
    generate_report(sorted_char_list, num_words)
   # print(text)
    #print(f"{num_words} words found in the document")
    #print(character_count)
    #print(report)
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    characters = {}
    lowered = text.lower()
    for letter in lowered:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters
def create_char_list(character_count):
    char_list = []
    for char, count in character_count.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)
    return char_list
def generate_report(sorted_char_list, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    for char_data in sorted_char_list:
        char = char_data["char"]
        num = char_data["num"]
        print(f"The '{char}' character was found {num} times")
    
    print("--- End report ---")
def sort_dict(char_list):
    return char_list["num"]


Main()
