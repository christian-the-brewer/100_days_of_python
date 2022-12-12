def fill_list():
    word_file = open('20k.txt')
    all_words = word_file.readlines
    text_list = []
    for word in all_words:
        text_list.append(word)
    word_list = [word[:-1] for word in text_list]
    return word_list

