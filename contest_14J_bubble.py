# Спринт 14
# J. Пузырёк


def bubble_sort(array):
    flag = True
    total_flag = False
    while flag:
        flag = False
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                flag = True
        if flag:
            total_flag = True
            print(*array)

    if not total_flag:
        print(*array)


def main():
    n = int(input())
    inp = input()
    bubble_sort([int(i) for i in inp.split()][:n])


def test():
    n = 5
    inp = '1 1 1 1 1'
    bubble_sort([int(i) for i in inp.split()][:n])


if __name__ == '__main__':
    # test()
    main()
#     test = """3 4 2 1 9
# 3 2 1 4 9
# 2 1 3 4 9
# 1 2 3 4 9
# """
