BITMAP: dict = {}
GRAPH_HEIGHT: int = 20
GRAPH_WIDTH: int = 10
MARGIN_WIDTH: int = 10
GRAPH_COUNT: int = 0

def calculate_cat_height(total_words: int, count: int) -> int:
    return int((GRAPH_HEIGHT / total_words) * count)

def add_char_data(text: str, x: int, y: int):
    text_length = len(text)
    width = GRAPH_WIDTH if GRAPH_WIDTH >= text_length else text_length
    for i in range(width + 1):
        if i < text_length:
            BITMAP[(i + 1 + x, y)] = text[i]
        else:
            BITMAP[(i + 1 + x, y)] = " "

def add_word_length_graph_data(small_words: int, med_words: int, big_words: int):
    global GRAPH_COUNT
    global GRAPH_WIDTH
    global GRAPH_HEIGHT
    global BITMAP

    GRAPH_COUNT += 1
    total_words = small_words + med_words + big_words
    small_height = calculate_cat_height(total_words, small_words)
    med_height = calculate_cat_height(total_words, med_words)
    big_height = calculate_cat_height(total_words, big_words)
    med_cat_loc = small_height
    big_cat_loc = med_cat_loc + med_height
    # XXX
    print()
    print(f"totalw {total_words}")
    print(f"smallh {small_height} medh {med_height} bigh {big_height}")
    print(f"medcatloc {med_cat_loc} bigcatloc {big_cat_loc}")
    for x in  range(GRAPH_WIDTH + 1):
        for y in  range(GRAPH_HEIGHT):
            if x == 0 or x == GRAPH_WIDTH:
                BITMAP[(x, y)] = "|"
            elif y == 0 or y == med_cat_loc or y == big_cat_loc or \
                y == GRAPH_HEIGHT:
                BITMAP[(x, y)] = "-"
            elif y == 1:
                add_char_data("Small words", 0, 1)
            elif y == med_cat_loc + 1:
                add_char_data("Medium words", 0, med_cat_loc + 1)
            elif y == big_cat_loc + 1:
                add_char_data("Big words", 0, big_cat_loc + 1)
            else:
                BITMAP[(x, y)] = " "

def add_cap_graph_data(cap_words: int, non_cap_words: int):
    global GRAPH_COUNT

    GRAPH_COUNT += 1
    total_words = cap_words + non_cap_words
    cap_words_height = calculate_cat_height(total_words, cap_words)
    non_cap_words_height = calculate_cat_height(total_words, non_cap_words)
    non_cap_words_loc = cap_words_height
    start_x = GRAPH_WIDTH + MARGIN_WIDTH
    # XXX
    print(f"startx {start_x}")
    print(f"graphc {GRAPH_COUNT}")
    print(f"capwh {cap_words_height} noncapwh {non_cap_words_height}")
    for x in range(GRAPH_WIDTH + 1):
        for y in range(GRAPH_HEIGHT):
            if x == 0 or x == GRAPH_WIDTH:
                BITMAP[(start_x + 1 + x, y)] = "|"
            elif y == 0 or y == non_cap_words_loc:
                BITMAP[(start_x + 1 + x, y)] = "-"
            elif y == 1:
                add_char_data("Capital Words", start_x + 1, 1)
            elif y == non_cap_words_loc + 1:
                add_char_data("Lower Case Words", start_x + 1, non_cap_words_loc + 1)

def graph():
    global GRAPH_WIDTH
    global GRAPH_COUNT
    global MARGIN_WIDTH
    global GRAPH_HEIGHT
    global BITMAP
    for y in  range(GRAPH_HEIGHT):
        for x in range(GRAPH_WIDTH * GRAPH_COUNT + MARGIN_WIDTH * GRAPH_COUNT):
            try:
                print(BITMAP[(x, y)], end="")
            except KeyError:
                print(" ", end="")
        print()