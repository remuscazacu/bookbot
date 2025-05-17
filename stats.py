import string


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_char(text):
    text = text.lower()
    counts = {}
    for letter in string.ascii_lowercase:
        counts[letter] = text.count(letter)

    return counts


def get_sorted_list(char_counts):
    sorted_list = sorted(
        [{"char": char, "num": count} for char, count in char_counts.items()],
        key=lambda x: x["num"],
        reverse=True,
    )
    return sorted_list
