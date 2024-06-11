def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_list = sorting(char_count)
    print(f"--- Begin report of books/frankenstein.txt ---\n {word_count} words found in the document\n {sorted_list}\n --- End report ---")
    


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
    

main()
