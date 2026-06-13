import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

# print(NUM_OR_DOT_REGEX.search('9'))
# print(NUM_OR_DOT_REGEX.search('a'))
# print(NUM_OR_DOT_REGEX.search('.'))

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def isEmpty(string: str):
    return len(string) == 0
