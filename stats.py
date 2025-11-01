def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_num_words(filepath):
    words = get_book_text(filepath).split()
    return len(words)

def count_characters(filepath):
    text = get_book_text(filepath)
    character_count = {}
    
    for char in text:
        if char.lower() not in character_count:
            character_count.update({char.lower(): 1})
        else:
            character_count[char.lower()] += 1
    return character_count

def sort_character_count(character_count):
    return dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    

