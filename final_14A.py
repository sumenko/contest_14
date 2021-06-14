# Спринт 14. Финальное задание
# A. Поиск в сломанном массиве

class UnknownRange(Exception):
    pass


def search(arr, m, begin, end):
    print('search: ', begin, end)
    if end - begin <= 1:
        if arr[end] == m:
            return end
        if arr[begin] == m:
            return begin
        return  -1
    mid = (begin + end) // 2
    left = arr[begin]
    center = arr[mid]
    right = arr[end]
    if (left < center and left <= m <= center):
        return search(arr, m, begin, mid)  # left
    elif (center <= right):# and center < m <= right:
        return search(arr, m, mid, end)  # right
    elif (left > center and (m < center or m > left)):
        return search(arr, m, begin, mid)  # left
    elif (center > right and (m >= center or m < right)): 
        return search(arr, m, mid, end)  # right
    
    # elif :
    #     return search(arr, m, mid)
    
    print(' '.join([f'{i:4}' for i in range(test[2])]))
    print(' '.join([f'{int(i):4}' for i in test[0].split()]), f'\tm = {test[1]}, answer = {test[3]}+')
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
    array = [int(i) for i in raw_array.split()[:n]]
    idx = search(array, m, 0, n - 1)
    return idx


def main():
    n = int(input())
    m = int(input())
    raw_array = input()

if __name__ == '__main__':
    tests = (
             ('10 11 12 13 1 2 3 4', 10, 8, 0, '#1.1'),
             ('10 11 12 13 1 2 3 4', 11, 8, 1, '#1.2'),
             ('10 11 12 13 1 2 3 4', 12, 8, 2, '#1.3'),
             ('10 11 12 13 1 2 3 4', 13, 8, 3, '#1.4'),
             ('10 11 12 13 1 2 3 4', 1, 8, 4, '#1.5'),
             ('10 11 12 13 1 2 3 4', 2, 8, 5, '#1.6'),
             ('10 11 12 13 1 2 3 4', 3, 8, 6, '#1.7'),
             ('10 11 12 13 1 2 3 4', 4, 8, 7, '#1.8'),
             ('10 11 12 13 1 2 3 4', 4, 8, 7, '#1.9'),
             ('10 11 12 13 1 2 3 4 5', 5, 9, 8, '#2.1'),
             ('10 11 12 13 1 2 3 4', 10, 9, 0, '#2.2'),
             ('10 11 12 13 1 2 3 4', 11, 9, 1, '#2.3'),
             ('10 11 12 13 1 2 3 4', 12, 9, 2, '#2.4'),
             ('10 11 12 13 1 2 3 4', 13, 9, 3, '#2.5'),
             ('10 11 12 13 1 2 3 4', 1, 9, 4, '#2.6'),
             ('10 11 12 13 1 2 3 4', 2, 9, 5, '#2.7'),
             ('10 11 12 13 1 2 3 4', 3, 9, 6, '#2.8'),
             ('10 11 12 13 1 2 3 4', 4, 9, 7, '#2.9'),
             ('10 11 12 13 1 2 3 4', 4, 9, 7, '#2.10'),
             ('2 3 4 50 1', 50, 5, 3),
             ('3 6 7', 8, 3, -1),
             ('13 14 15 5 6 7 8 9 10 11 12', 11, 10, 9, '#'),
             ('1 2 3 4 5 6 7 8 9 10 0', 1, 11, 0, '#38'),
             ('19 21 100 101 1 4 5 7 12', 50, 9, -1),
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
        except UnknownRange:
            print('Assertion error in test', test[4])
            print('unknown range error')
            break
        except AssertionError:
            print('Assertion error in test', test[4])
            print('wrong answer')
            print(' '.join([f'{i:4}' for i in range(test[2])]))
            print(' '.join([f'{int(i):4}' for i in test[0].split()]), f'\tm = {test[1]}, answer = {idx}- ? {test[3]}+')
            break
    # main()

