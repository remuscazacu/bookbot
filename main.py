import sys
from stats import get_num_words, get_num_char, get_sorted_list


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    print("================ BOOKBOT =====================")
    print(f"Analysing book found at {filepath}")
    print("---------------- Word Count ------------------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("---------------- Character Count -------------")

    letter_counts = get_num_char(text)
    sorted_char_data = get_sorted_list(letter_counts)

    for entry in sorted_char_data:
        print(f"{entry['char']}: {entry['num']}")


if __name__ == "__main__":
    main()
