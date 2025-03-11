def difference(*args: int|float) -> int|float:
    if len(args) == 0:
        return 0
    min = args[0]
    max = args[0]
    for i in args:
        if min >= i:
            min = i
        if max <=i:
            max = i
    return round(max - min, 2)
