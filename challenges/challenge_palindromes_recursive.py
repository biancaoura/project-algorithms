def is_palindrome_recursive(
        word: str, low_index: int, high_index: int
) -> bool:
    if low_index > high_index and word:
        return True

    try:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
    except IndexError:
        return False
