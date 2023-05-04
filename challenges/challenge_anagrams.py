def merge_sort(string: str) -> str:
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left: str, right: str) -> str:
    result = []
    l_index, r_index = 0, 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1

    result += left[l_index:]
    result += right[r_index:]

    return "".join(result)


def is_anagram(first_string: str, second_string: str):
    first_sort = merge_sort(first_string.lower())
    second_sort = merge_sort(second_string.lower())

    if not first_sort or not second_sort:
        return (first_sort, second_sort, False)

    return (
        first_sort,
        second_sort,
        first_sort == second_sort,
    )
