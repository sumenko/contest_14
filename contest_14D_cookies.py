# Спринт 14
# D. Печеньки

def how_many_happy(greed, cookies):
    happy_children = 0
    greed.sort()
    cookies.sort()
    g = len(greed) - 1
    c = len(cookies) - 1
    while g >= 0 and c >= 0:
        if cookies[c] >= greed[g]:
            happy_children += 1
            g -= 1
        else:
            g -= 1
            continue
        c -= 1

    return happy_children


def main():
    n = int(input())
    greed = [int(i) for i in input().split()]
    m = int(input())
    cookies = [int(i) for i in input().split()]
    print(how_many_happy(greed[:n], cookies[:m]))


if __name__ == '__main__':
    tests = (
        ([1, 2], [2, 1, 3], 2),
        ([2, 1, 3], [1, 1], 1),
        ([4], [1,4,7,10,2,2,7,8], 1),
        ([8, 5, 5, 8, 6, 9, 8, 2, 4, 7], [9, 8, 1, 1, 1, 5, 10, 8], 5)
    )
    for greed, cookies, result in tests:
        assert how_many_happy(greed, cookies) == result
    main()
