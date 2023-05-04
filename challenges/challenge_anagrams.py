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
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]

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
