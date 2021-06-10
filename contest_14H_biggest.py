# Спринт 14
# H. Большое число

def compare(i1, i2):
    if i1 + i2 > i2 + i1:
        return True
    return False


def insertion_sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and compare(item, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item
    return array

def get_biggest(arr, n):
    numbers = arr.split()[:n]
    insertion_sort(numbers)
    return ''.join(numbers)


def main():
    n = int(input())
    print(get_biggest(input(), n))


if __name__ == '__main__':
    assert get_biggest('15 56 2', 3) == '56215'
    assert get_biggest('1 783 2', 3) == '78321'
    assert get_biggest('2 4 5 2 10', 5) == '542210'
    assert get_biggest('82 58 66 34 64 37 40 97 93 52 28 98 90 64 19 22 21 83 56 70 46 17 31 51 55 41 68 18 98 89 88 74 6 6 31 36 35 8', 38) == '9898979390898888382747068666664645856555251464140373635343131282221191817'
    assert get_biggest('9 18 1 65 51 16 6 43 6 36 7 11 64 5 1 76 15 11 11 15 57 95 3 49 92 78 83 51 10 3', 30) == '995928378776666564575515149433633181615151111111110'
    main()
