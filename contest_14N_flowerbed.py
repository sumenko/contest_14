# 14 Спринт
# N. Клумбы

def txt_to_list(txt):
    lines = txt.split('\n')
    n = int(lines[0])
    arr = []
    for k  in range(1, n + 1):
        if lines[k] != '':
            arr.append([int(i) for i in lines[k].split()])
    return arr


def get_flower_bed(arr):
    arr.sort(key=lambda k: k[0])
    answer = [arr[0], ]
    for i in range(1, len(arr)):
        if answer[-1][1] >= arr[i][0]:
            answer[-1][1] = max(answer[-1][1], arr[i][1])
        else:
            answer.append(arr[i])
    for a in answer:
        print(*a)


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append([int(i) for i in input().split()])
    get_flower_bed(arr)


if __name__=='__main__':
    tests = ("""4
7 8
7 8
2 3
6 10
""", """4
2 3
5 6
3 4
3 4
""", """6
1 3
3 5
4 6
5 6
2 4
7 10
""")
    # for t in tests:
    #     get_flower_bed(txt_to_list(t))
    # get_flower_bed([[7,8], [7,8], [2,3], [6,10]])
    main()
