def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_list = sorting(char_count)
    print_report(sorted_list, word_count, book_path)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter +=1
    return counter

def count_chars(text):
    lower_case = text.lower()
    char_counter_dict = {}
    count_for_char = 0
    for i in lower_case:
        if i not in char_counter_dict:
            count_for_char = 1
            
        if i in char_counter_dict:
            count_for_char += 1
        char_counter_dict.update({i:count_for_char})
    return char_counter_dict

def sorting(char_counter_dict):
    dict_list = []
    for key, value in char_counter_dict.items():
        if key.isalpha():
            dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dictionary):
    return dictionary["num"]

def print_report(dict_list, word_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    
    # Iterating the sorted list of dictionaries to print each character count
    for entry in dict_list:
        char = entry["char"]
        count = entry["num"]
        print(f"The '{char}' character was found {count} times")
    
    print(f"--- End report ---")

    

main()
