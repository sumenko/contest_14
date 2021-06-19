# Спринт 14
# B. Эффективная быстрая сортировка
# ID: 51984399

from random import randint


def gte(a, b):
    """ Сравнение участников True если a > b """
    login_a, p_a, f_a = a
    login_b, p_b, f_b = b

    if (p_a > p_b or (p_a == p_b and f_a < f_b) or
       (p_a == p_b and f_a == f_b and login_a < login_b)):
        return True
    return False


def lte(a, b):
    """ Сравнение участников True если a < b """
    return not gte(a, b)


class QuickSort():
    def __init__(self, gte_func=None, lte_func=None, reverse=False):
        if not gte_func:
            self.gte = lambda a, b: a > b
        else:
            self.gte = gte

        if not lte_func:
            self.lte = lambda a, b: a < b
        else:
            self.lte = lte

        if reverse:
            self.lte, self.gte = self.gte, self.lte

    def sort(self, arr, left=0, right=None):
        if not right:
            right = len(arr) - 1
        pivot = arr[randint(left, right)]
        l_ptr = left
        r_ptr = right

        while l_ptr <= r_ptr:
            while self.lte(arr[l_ptr], pivot) and l_ptr < right:
                l_ptr += 1
            while self.lte(pivot, arr[r_ptr]) and r_ptr > left:
                r_ptr -= 1

            if l_ptr <= r_ptr:
                arr[l_ptr], arr[r_ptr] = arr[r_ptr], arr[l_ptr]
                l_ptr += 1
                r_ptr -= 1

        if r_ptr > left:
            self.sort(arr, left, r_ptr)
        if l_ptr < right:
            self.sort(arr, l_ptr, right)


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        login, p, f = input().split()
        arr.append((login, int(p), int(f)))
    q = QuickSort(gte_func=gte, lte_func=lte, reverse=True)
    q.sort(arr)
    for user in arr:
        print(user[0])


if __name__ == '__main__':
    main()
