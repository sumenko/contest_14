# Спринт 14
# D. Печеньки

def how_many_happy(children, cookies):
    happy_children = 0
    children.sort()
    cookies.sort()
    i = 0
    k = 0
    print(*children)
    print(*cookies)
    while i < len(children) and k < len(cookies):
        print('children[{}]={} cookies[{}]={} :{}'.format(i, children[i], k, cookies[k], happy_children))
        if children[i] == cookies[k]:
            happy_children += 1
            i += 1
            k += 1
        elif children[i] > cookies[k]:
            k += 1
        elif children[i] < cookies[k]:
            i += 1

    print(happy_children)


def main():
    n = int(input())
    children = input().split()
    m = int(input())
    cookies = input().split()
    how_many_happy(children[:n], cookies[:m])


if __name__ == '__main__':
    # how_many_happy([1, 2], [2, 1, 3])
    # how_many_happy([2, 1, 3], [1, 1])
    how_many_happy([8, 5, 5, 8, 6, 9, 8, 2, 4, 7], [9, 8, 1, 1, 1, 5, 10, 8])
    # main()
