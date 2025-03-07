import keyword
import string


def variable_name(variable_name: str) -> bool:
    if variable_name in keyword.kwlist:
        return False

    if variable_name.count('_') > 1:
        return False

    if not variable_name:
        return False

    if variable_name[0].isdigit():
        return False

    allowed_characters = set(string.ascii_lowercase + string.digits + '_')
    if not set(variable_name).issubset(allowed_characters):
        return False

    return True
