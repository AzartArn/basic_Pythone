def second_index(text: str, some_str: str) -> int|None:
    index1 = text.find(some_str)
    if index1 != -1:
        index2 = text.find(some_str, index1+1)
        if index2 != -1:
            return index2
    return None

