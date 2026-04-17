import re

def get_graph_flag(text):

    flag = 0

    # Rule 1: very high amount
    numbers = list(map(int, re.findall(r"\d{3,}", text)))
    if numbers and max(numbers) > 100000:
        flag = 1

    # Rule 2: suspicious repetition (simple)
    words = text.lower().split()
    if words.count("ltd") > 3:
        flag = 1

    return flag