import sys
from stats import get_word_count, get_char_count, sort_char_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(filepath, word_count, chars):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}...')
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for c in chars:
        if c["key"].isalpha():
            print(f'{c["key"]}: {c["value"]}')
    print("============= END ===============")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    frankenstein = get_book_text(filepath)
    word_count = get_word_count(frankenstein)
    char_count = sort_char_list(get_char_count(frankenstein))

    print_report(filepath, word_count, char_count)
    
main()