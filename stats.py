def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_num_words(filepath):
    words = get_book_text(filepath).split()
    return len(words)

def count_characters(filepath):
    text = get_book_text(filepath)
    character_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        " ": 0,
        ".": 0,
        ",": 0,
        "!": 0,
        "?": 0,
    }
    for char in text:
        if char.lower() in character_count:
            character_count[char.lower()] += 1
    return character_count

def sort_character_count(character_count):
    return dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    

