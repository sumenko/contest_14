from random import expovariate, randint, randrange


def print_arr(arr, left, right):
    print(''.join([f'{i:<4}' for i in arr]))

    s = ['.'] * len(arr)
    s[left] = 'l'
    if left != right: 
        s[right] = 'r'
    else:
        s[left] = '*'
    print(''.join([f'{i:<4}' for i in s]), '\n')


def quick_sort(arr, left=0, right=None):
    if not right:
        right = len(arr) - 1
    pivot = arr[randint(left, right)]
    l = left
    r = right

    while l <= r:
        while arr[l] < pivot and l < right:
            l += 1
        while pivot <arr[r] and r > left:
            r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    if r > left:
        quick_sort(arr, left, r)
    if l < right:
        quick_sort(arr, l, right)




if __name__ == '__main__':
    tests = (
        [4, 8, 9, 20, 1, 5, 3, 10],
        [1, 2, 0, 4, 5],
        [1, 2, 3, 4, 5],
        [0, 2, 3, 4, 5],
        [1, 0, 3, 4, 5],
        [1, 2, 3, 0, 5],
        [1, 2, 3, 4, 0],
        [randint(0, 10) for _ in range(10)],
    )
    for n, test in enumerate(tests):
        print('Test #', n)
        quick_sort(test, 0, len(test) - 1)
        try:
            srt = sorted(test)
            assert test == srt
        except AssertionError:
            print(*test, '!=', *srt)
        
