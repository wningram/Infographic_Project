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


def main():
    words = get_words()
    word_counts = get_word_count(words)
    print(get_most_frequent_small_word(word_counts))
    print(get_most_frequent_medium_word(word_counts))
    print(get_most_frequent_large_word(word_counts))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program terminated.")