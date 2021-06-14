# Спринт 14. Финальное задание
# A. Поиск в сломанном массиве

class UnknownRange(Exception):
    pass


def search(arr, m, begin, end):
    print('search: ', begin, end)
    if end - begin < 2:
        if arr[end] == m:
            return end
        if arr[begin] == m:
            return begin
        return  -1
# 0 1 2
# 3 6 7  ?8
# begin = 0 end = 2 mid = 1 left = 3 right = 7 
# 
# 
#
#
    mid = (begin + end) // 2
    left = arr[begin]
    center = arr[mid]
    right = arr[end]
    if left < center and left < m < center:
        return search(arr, m, begin, mid)
    elif center < right and center < m <= right:
        return search(arr, m, mid, end)
    print(f'look for {m}')
    print(f'begin: {begin} mid: {mid} end: {end}')
    print(f'left: {left} center: {center} right: {right}')
    raise UnknownRange
    # elif left >= center and (center > m):
    #     return search(arr, m, begin, mid)
    # elif center >= right and (m > center):
    #     return search(arr, m, mid, end)
    # return arr[mid]


def search_idx(raw_array, m, n):
    # print(n)
    array = [int(i) for i in raw_array.split()[:n]]
    # print(array)
    idx = search(array, m, 0, n - 1)
    # center = array[mid]
    return idx


def main():
    n = int(input())
    m = int(input())
    raw_array = input()
    # print(search_idx(raw_array, m, n))

if __name__ == '__main__':
    tests = (
             ('3 6 7', 8, 3, -1),
             ('13 14 15 5 6 7 8 9 10 11 12', 11, 10, 9, '#'),
             ('1 2 3 4 5 6 7 8 9 10 0', 1, 11, 0, '#38'),
             ('19 21 100 101 1 4 5 7 12', 50, 9, -1),
             ('2 3 4 50 1', 50, 5, 3),
             ('21 100 101 1 4 5 7 12 19', 5, 9, 5),
             ('19 21 100 101 1 4 5 7 12', 50, 9, -1),
             ('6 7 10 0 2 4 5', 3, 7, -1),
             ('1', 4, 1, -1),
             ('3 5 6 7 9 1 2', 4, 7, -1),
             ('19 21 100 101 1 4 5 7 12', 5, 9, 6),
             ('1 2 3 50 0', 50, 5, 3),
             )

    for n, test in enumerate(tests):
        print('test ', n+1)
        try:
            idx = search_idx(test[0], test[1], test[2])
            assert idx == test[3]
        except AssertionError:
            print('Assertion error')
            print(' '.join([f'{i:4}' for i in range(test[2])]))
            print(' '.join([f'{int(i):4}' for i in test[0].split()]), f'\tm = {test[1]}, answer = {idx}- ? {test[3]}+')
            break
    # main()

