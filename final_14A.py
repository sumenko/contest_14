# Спринт 14. Финальное задание
# A. Поиск в сломанном массиве
# Бинарный поиск в сломанном упорядоченном массиве (смещенный кольцевой буфер)
# ID попытки: 51953142

def search(arr, m, begin, end):
    """ Рекурсивный поиск в сломанном массиве"""
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

    if left < center < right:  # отсортированный по возрастанию массив
        if m < center:
            return search(arr, m, begin, mid)  # left
        else:
            return search(arr, m, mid, end)  # right
    elif left < center > right:  # неправильная правая сторона
        if left <= m <= center:  # идем влево только тогда когда уверены
            return search(arr, m, begin, mid)  # left
        else:
            return search(arr, m, mid, end)  # right
    elif left > center < right:  # неправильная левая сторона
        if center <= m <= right:  # идем вправо только тогда когда уверены
            return search(arr, m, mid, end)  # right
        else:
            return search(arr, m, begin, mid)  # left


def search_idx(raw_array, m, n):
    """ обёртка для поиска в сломанном массиве """
    array = [int(i) for i in raw_array.split()[:n]]
    idx = search(array, m, 0, n - 1)
    return idx


def main():
    n = int(input())
    m = int(input())
    raw_array = input()
    print(search_idx(raw_array, m, n))


if __name__ == '__main__':
    main()
