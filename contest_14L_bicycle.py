# Два велосипеда

def bin_search(arr, num, left, right):
    """ Бинарный поиск num, arr - неубывающий список """
    if right <= left:
        return -1
    mid = (right + left) // 2
    if arr[mid] == num:
        return mid
    elif num < arr[mid]:
        # go left
        return bin_search(arr, num, left, mid)
    else:
        # go right
        return bin_search(arr, num, mid + 1, right)


def which_day(n, money, cost):
    arr = [int(num) for num in money.split()]
    a = bin_search(arr[:n], cost, 0, n)
    # print('look for nearest greater than _{}_ in {}. result: {}'.format(cost, money, a))
    return a


if __name__ == '__main__':
    assert which_day(6, '1 2 4 4 6 8', 1) == 0
    assert which_day(6, '1 2 4 4 6 8', 2) == 1
    assert which_day(6, '1 2 4 4 6 8', 4) == 3
    assert which_day(6, '1 2 4 4 6 8', 6) == 4
    assert which_day(6, '1 2 4 4 6 8', 8) == 5
    assert which_day(6, '1 2 4 4 6 8', 3) == -1
    # print(which_day(6, '1 2 4 4 6 8', 3))
    # assert which_day(6, '1 2 4 4 6 8', 3) == (3, 5)
    # assert which_day(6, '1 2 4 4 4 4', 3) == (3, -1)
    # assert which_day(6, '1 2 4 4 4 4', 10) == (-1, -1)
