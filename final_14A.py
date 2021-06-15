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
        return -1
    mid = (begin + end) // 2
    left = arr[begin]
    center = arr[mid]
    right = arr[end]

    if left < center < right:
        print('sorted array')
        if m < center:
            return search(arr, m, begin, mid)  # left
        else:
            return search(arr, m, mid, end)  # right
    elif left < center > right:
        print('wrong right')
        if left <= m <= center:
            print('go left <<')
            return search(arr, m, begin, mid)  # left
        else:
            print('go right >>')
            return search(arr, m, mid, end)  # right
    elif left > center < right:
        print('wrong left')
        if center <= m <= right:
            print('go right >>>>')
            return search(arr, m, mid, end)  # right
        else:
            print('go left <<<<')
            return search(arr, m, begin, mid)  # left


    print('*'*50)
    print(' '.join([f'{i:4}' for i in range(test[2])]))
    print(' '.join([f'{int(i):4}' for i in test[0].split()]), f'\tm = {test[1]}, answer = {test[3]}+')
    print(f'look for {m}')
    print(f'begin: {begin} mid: {mid} end: {end}')
    print(f'left: {left} center: {center} right: {right}')
    raise UnknownRange


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
             ('1 2 3', 1, 3, 0, 'sorted 1'),
             ('1 2 3', 2, 3, 1, 'sorted 2'),
             ('1 2 3', 3, 3, 2, 'sorted 3'),
             ('1 2 3', 4, 3, -1, 'sorted 4'),
             ('1 2 3', 0, 3, -1, 'sorted 5'),
             ('55 56 5', 5, 3, 2, '$1'),
             ('55 56 5', 55, 3, 0, '$2'),
             ('55 56 5', 56, 3, 1, '$3'),
             ('55 56 5', 54, 3, -1, '$4'),
             ('55 56 5', 57, 3, -1, '$5'),
             ('55 56 5', 4, 3, -1, '$6'),
             ('55 56 5', 6, 3, -1, '$7'),
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
             ('10 11 12 13 1 2 3 4 5', 10, 9, 0, '#2.2'),
             ('10 11 12 13 1 2 3 4 5', 11, 9, 1, '#2.3'),
             ('10 11 12 13 1 2 3 4 5', 12, 9, 2, '#2.4'),
             ('10 11 12 13 1 2 3 4 5', 13, 9, 3, '#2.5'),
             ('10 11 12 13 1 2 3 4 5', 1, 9, 4, '#2.6'),
             ('10 11 12 13 1 2 3 4 5', 2, 9, 5, '#2.7'),
             ('10 11 12 13 1 2 3 4 5', 3, 9, 6, '#2.8'),
             ('10 11 12 13 1 2 3 4 5', 4, 9, 7, '#2.9'),
             ('10 11 12 13 1 2 3 4 5', 4, 9, 7, '#2.10'),
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
        test_name = '=' * 10 + ' Test ' + str(n+1) + '. '
        try:
            test_name += test[4] + ' '
        except IndexError:
            pass
        test_name += '=' * 10
        print(test_name)
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

