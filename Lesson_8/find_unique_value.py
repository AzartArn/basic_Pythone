def find_unique_value(some_list: list[int|float]) -> int|float:
    unique = 0
    for i in range(len(some_list)):
        unique = some_list[i]
        count = 0
        for j in range(len(some_list)):
            if unique == some_list[j]:
                count += 1
        if count == 1:
            break
    return unique

