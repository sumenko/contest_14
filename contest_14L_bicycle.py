# Спринт 14
# L. Два велосипеда
# в отличии от бинарного поиска убрано строгое равенство num == arr[mid]

def bin_search(arr, num, left, right):
    """ Бинарный поиск num, arr - неубывающий список """
    if right <= left:
        if left == len(arr):
            return -1
        return left + 1

    mid = (right + left) // 2
    if num <= arr[mid]:
        # go left
        return bin_search(arr, num, left, mid)
    else:
        # go right
        return bin_search(arr, num, mid + 1, right)


def which_day(n, money, cost):
    arr = [int(num) for num in money.split()]
    a = bin_search(arr[:n], cost, 0, n)
    b = bin_search(arr[:n], cost * 2, 0, n)
    return a, b


def main():
    n = int(input())
    money = input()
    cost = int(input())
    print(*which_day(n, money, cost))


if __name__ == '__main__':
    main()
    assert which_day(6, '1 2 4 4 6 8', 1) == (1, 2)
    assert which_day(6, '1 2 4 4 6 8', 2) == (2, 3)
    assert which_day(6, '1 2 4 4 6 8', 4) == (3, 6)
    assert which_day(6, '1 2 4 4 6 8', 6) == (5, -1)
    assert which_day(6, '1 2 4 4 6 8', 8) == (6, -1)
    assert which_day(6, '4 4 4 4 6 8', 4) == (1, 6)
    assert which_day(6, '4 4 4 4 6 6', 4) == (1, -1)


    assert which_day(6, '1 2 4 4 6 8', 3) == (3, 5)
    assert which_day(6, '1 2 4 4 4 4', 3) == (3, -1)
    assert which_day(6, '1 2 4 4 4 4', 10) == (-1, -1)
