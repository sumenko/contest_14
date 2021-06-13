# Спринт 14. Финальное задание
# A. Поиск в сломанном массиве


def search(raw_array, n, m):
    array = raw_array.split()[n]


    idx = -1
    return idx


def main():
    pass


if __name__ == '__main__':
    assert search('19 21 100 101 1 4 5 7 12', 9, 5) == 6
    assert search('21 100 101 1 4 5 7 12 19', 9, 5) == 5
    assert search('19 21 100 101 1 4 5 7 12', 9, 50) == -1
