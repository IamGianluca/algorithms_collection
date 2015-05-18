def bubble_sort(L):
    """ (list) -> NoneType

    Sort list from smallest to largest using bubble sort algorithm

    :param L: unsorted list

    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    # The index of the last unsorted item
    begin = 0
    end = len(L) - 1

    while end != 0:

        # Bubble once through the unsorted section to move the largest item in index end
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]

        end -= 1


if __name__ == "__main_":
    import doctest
    doctest.testmod()