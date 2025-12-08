def get_num_words(raw_read:str)->int:
    if not raw_read:
        return 0
    
    text_string = str(raw_read)
    if not text_string or not isinstance(text_string, str):
        return 0
    return len(text_string.split())

def get_char_count(raw_read:str)-> dict:
    characters = {}
    if not isinstance(raw_read, str) or not raw_read:
        return {}
    book_text = list(raw_read)
    for char in book_text:
        char_lowered = char.lower()
        if char_lowered in characters:
            characters[char_lowered] += 1
        else:
            characters[char_lowered] = 1
    return characters

def get_sorted_char_count(characters_count: dict)->dict:
    if not characters_count or not isinstance(characters_count, dict):
        return {}
    return {k: v for k, v in sorted(characters_count.items(), key=lambda item: (item[1],item[0]), reverse=True)}