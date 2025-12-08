import sys
from stats import get_num_words, get_char_count, get_sorted_char_count

def get_book_text(path_to_file):
    # characters = {}
    with open(path_to_file) as f:
        file_contents = f.read() #read per character
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    # for key, value in get_book_text(file_path):
    #     print(f"key: {key}, value: {value}")
    book_text = get_book_text(file_path)
    num_of_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    # print(char_count)
    report_components = ["============ BOOKBOT ============",
                         f"Analyzing book found at {file_path}...",
                         "----------- Word Count ----------",
                         f"Found {num_of_words} total words",
                         "--------- Character Count -------",
                         ]
    for component in report_components:
        print(component)
    for k, v in get_sorted_char_count(char_count).items():
        if not k.isalnum() and not k.isalpha():
            continue
        print(f"{k}: {v}")
    # # return counts

if __name__ == "__main__":
    main()