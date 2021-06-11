# 14 Спринт
# G. Гардероб

def sorted_gard(arr, n=None):
    counter = {}
    arr = arr.split()
    if n:
        arr = arr[:n]
    for item in arr:
        try:
            counter[item] += 1
        except KeyError:
            counter[item] = 1
    return [' '.join(k * counter[k]) for k in sorted(counter.keys())]


def main():
    n = int(input())
    arr = input()
    print(*sorted_gard(arr, n))


if __name__ == '__main__':
    # print(*sorted_gard('2 1 1 2 0 2'))
    # print(*sorted_gard('0 2 1 2 0 0 1'))
    main()
