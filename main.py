def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    char_count = count_chars(text)
    print(f"This text contains {word_count} words")
    print(f"This text containts {char_count} characters")


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
            char_counter_dict.update({i:count_for_char})
        if i in char_counter_dict:
            count_for_char += 1
            char_counter_dict.update({i:count_for_char})
    return char_counter_dict

main()
