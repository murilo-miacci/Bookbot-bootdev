def count_words(text: str) -> int:
    words = text.split()

    return len(words)


def count_characters(text: str) -> list[tuple[str, int]]:
    text = text.lower()

    counter = {}
    for character in text:
        if character.isalpha():
            if character not in counter:
                counter[character] = 1
            else:
                counter[character] += 1

    list_counter = []
    for key, value in counter.items():
        list_counter.append((key, value))

    return list_counter


def sort_on(info: tuple[str, int]) -> int:
    return info[1]
