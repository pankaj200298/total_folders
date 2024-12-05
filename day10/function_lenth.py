


def get_count_small_words (input_strings , max_len = 3):

    small_words = []
    for words in input_strings.split():
        if len(words) <= max_len :
            small_words.append(words)
            print(small_words)

    return len(small_words)

joke = "I swear I couldn’t love you more than I do right now, and yet I know I will tomorrow."
joke_words = get_count_small_words(joke, max_len= 7)
print(joke_words)
