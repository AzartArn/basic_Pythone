import re

hashtag = input('Введіть рядок: ')

hashtag = re.sub(r"[^a-zA-Z\s]", "", hashtag)
hashtag = "".join(hashtag.title().split())
hashtag = "#" + hashtag
hashtag = hashtag[:140]

print(hashtag)

