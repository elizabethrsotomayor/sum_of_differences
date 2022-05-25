def sum_of_differences(arr: list) -> int:
    """
    Sum the differences between consecutive pairs in the array in descending order.
    :param arr: unsorted list
    :return: total of differences
    """
    if len(arr) == 0 or len(arr) == 1:
        return 0
    else:
        s = sorted(arr, reverse=True)
        first = s[0]
        total = 0
        for i in range(1, len(s)):
            total += (first - s[i])
            first = s[i]

        return total
