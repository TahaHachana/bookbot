BOOK_PATH = "books/frankenstein.txt"


def read_file(path):
    with open(path) as f:
        return f.read()


def word_count(str):
    words = str.split()
    return len(words)


def count_letters(str):
    letter_count = {}
    for letter in str.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


def tuple_snd(tuple):
    return tuple[1]


def dict_to_sorted_tuple_list(dict):
    return sorted(dict.items(), key=tuple_snd, reverse=True)


def print_tuple_list(tuple_list):
    for tuple in tuple_list:
        fst, snd = tuple
        print(f"The '{fst}' character appears {snd} times")


def main():
    text = read_file(BOOK_PATH)
    words = word_count(text)
    letters = count_letters(text)
    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"{words} words found in the document")
    print("")
    print_tuple_list(dict_to_sorted_tuple_list(letters))
    print("--- End report ---")


main()
