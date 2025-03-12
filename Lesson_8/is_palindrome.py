import re


def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = re.sub(r'[^a-zA-Zа-яА-ЯёЁ0-9]', '', text)
    for i in range(int(len(text)/2)+1):
        if text[i] != text[-(i+1)]:
            return False
    return True

