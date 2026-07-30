from sys import argv, exit

from stats import *


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        file_content = file.read()
    return file_content


def print_report(
    file_path: str, word_count: int, sorted_list: list[tuple[str, int]]
) -> None:
    print(" ============ BOOKBOT ============")
    print(f" Analyzing {file_path}...\n")
    print(" ----------- Word Count ----------")
    print(f"     Found {word_count} total words\n")
    print(" -------- Character Count --------\n")
    for i in range(0, len(sorted_list) - 1, 2):
        if sorted_list[i][0].isalpha():
            print(
                f" {' ':<3}{sorted_list[i][0]}: {sorted_list[i][1]:^7}       "
                f" {sorted_list[i + 1][0]}: {sorted_list[i + 1][1]:^7}"
            )
    print("\n ============= END ===============\n")


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    file_path = argv[1]

    text = get_book_text(f"{file_path}")
    total_words = count_words(text)

    list_counter = count_characters(text)
    sorted_list_counter = sorted(list_counter, reverse=True, key=sort_on)

    print_report(f"{file_path}", total_words, sorted_list_counter)


if __name__ == "__main__":
    main()
