from stats import count_words, count_chars, alpha_count_index
import sys


def get_book_text(path):
    with open(path) as f:
        res = f.read()
    return res


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    # cont = get_book_text("./books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt...")
    # cont = get_book_text("./books/frank.txt")
    cont = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    cnt = count_words(cont)
    print(f"Found {cnt} total words")
    print("--------- Character Count -------")
    cntdic = count_chars(cont)
    srtdic = alpha_count_index(cntdic)
    for pr in srtdic:
        print(f"{pr['char']}: {pr['count']}")
    print("============= END ===============")

main()