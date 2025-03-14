def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    text = text.lower()
    chars = {}

    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars

def sort_on(dict):
    return dict["value"]

def sort_char_list(chars):

    chars_list = [{"key": k, "value": v} for k, v in chars.items()]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list