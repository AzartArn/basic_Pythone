def add_one(some_list: list[int]) -> list[int]:
    tmp_str = ""
    for i in some_list:
        tmp_str = tmp_str + str(i)
    tmp_str = str(int(tmp_str) + 1)
    return [int(tmp_str[i]) for i in range(len(tmp_str)) ]

