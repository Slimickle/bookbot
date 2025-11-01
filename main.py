import sys

from stats import get_num_words, count_characters, sort_character_count

def main():

    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    word_count = count_characters(filepath)
    word_count = sort_character_count(word_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")
    for char, count in word_count.items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()