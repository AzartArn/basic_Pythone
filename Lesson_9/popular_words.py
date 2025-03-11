def popular_words(text: str, words: list[str]) -> dict[str, int]:
    result_list = {}
    text_list = text.lower().split()
    for i in words:
        count = 0
        for j in text_list:
            if i == j:
                count += 1
        result_list[i] = count
    return result_list
