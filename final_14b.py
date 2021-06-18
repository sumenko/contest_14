from random import expovariate, randint, randrange


def gte(a, b):
    login_a, p_a, f_a = a
    login_b, p_b, f_b = b
    print(login_a, login_b)
    if (p_a > p_b or  (p_a == p_b and f_a < f_b) or
        (p_a == p_b and f_a == f_b and login_a < login_b)):
        return True
    return False


def lte(a, b):
    return gte(b, a)


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


def main():
    pass

if __name__ == '__main__':
    main()
        
# """5
# alla 4 100
# gena 6 1000
# gosha 2 90
# rita 2 90
# timofey 4 80
# """
