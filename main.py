import graph

INPUT_FILE = "file.txt"

def get_words() -> list:
    """
    Reads in a file and produces a list of lines split into a sublist of
    words.
    """
    result = []
    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            cleaned_line = line.replace("\n", "")
            [result.append(word) for word in cleaned_line.split()]
    return result

def get_word_count(words: list) -> dict:
    result = {}
    for word in words:
        if word in result.keys():
            result[word] = result[word] + 1
        else:
            result[word] = 1
    return result

def get_most_frequent_small_word(word_counts: dict) -> tuple:
    result = (None, 0)
    for word, count in word_counts.items():
        if len(word) > 0 and len(word) <= 4:
            if count > result[1]:
                result = (word, count)
    return result

def get_most_frequent_medium_word(word_counts: dict) -> tuple:
    result = (None, 0)
    for word, count in word_counts.items():
        if len(word) >= 5 and len(word) <= 7:
            if count > result[1]:
                result = (word, count)
    return result

def get_most_frequent_large_word(word_counts: dict) -> tuple:
    result = (None, 0)
    for word, count in word_counts.items():
        if len(word) >= 8:
            if count > result[1]:
                result = (word, count)
    return result

def get_unique_non_cap(word_counts: dict) -> int:
    count = 0
    for word in word_counts.keys():
        first_letter: str = word[0]
        if not first_letter.isupper():
            count += 1
    return count

def get_unique_cap(word_counts: dict) -> int:
    count = 0
    for word in word_counts.keys():
        first_letter: str = word[0]
        if first_letter.isupper():
            count += 1
    return count

def count_small_words(word_counts: dict) -> int:
    total_count = 0
    for word, count in word_counts.items():
        if len(word) > 0 and len(word) <= 4:
            total_count += count
    return total_count

def count_med_words(word_counts: dict) -> int:
    total_count = 0
    for word, count in word_counts.items():
        if len(word) >= 5 and len(word) <= 7:
            total_count += count
    return total_count

def count_big_words(word_counts: dict) -> int:
    total_count = 0
    for word, count in  word_counts.items():
        if len(word) >= 8:
            total_count += count
    return total_count

def print_header():
    words = get_words()
    word_counts = get_word_count(words)
    smallWord, smallCount = get_most_frequent_small_word(word_counts)
    medWord, medCount = get_most_frequent_medium_word(word_counts)
    bigWord, bigCount = get_most_frequent_large_word(word_counts)
    print("file.txt")
    print(f"Total Unique Words: {len(word_counts.keys())}")
    print(f"Most used words (s/m/b): {smallWord} ({smallCount}x) ", end='')
    print(f"{medWord} ({medCount}x) ", end="")
    print(f"{bigWord} ({bigCount}x)")
    print()

def main():
    words = get_words()
    word_counts = get_word_count(words)
    small_words_count = count_small_words(word_counts)
    med_words_count = count_med_words(word_counts)
    big_words_count = count_big_words(word_counts)

    cap_words = get_unique_cap(word_counts)
    non_cap_words = get_unique_non_cap(word_counts)

    print_header()

    # XXX
    print(f"Small Words: {small_words_count}")
    print(f"Med Words: {med_words_count}")
    print(f"Big Words: {big_words_count}")

    graph.add_word_length_graph_data(
        small_words_count,
        med_words_count,
        big_words_count
    )
    graph.add_cap_graph_data(
        cap_words,
        non_cap_words
    )
    graph.graph()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program terminated.")