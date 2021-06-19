# Спринт 14
# B. Эффективная быстрая сортировка
# ID: 51984399

from random import randint


class Member():
    def __init__(self, login, p, f):
        self.login = login
        self.solved = p
        self.fine = f

    def __gt__(self, obj):
        if (self.solved > obj.solved or
            (self.solved == obj.solved and self.fine < obj.fine) or
            ((self.solved == obj.solved and self.fine == obj.fine and
             self.login < obj.login))):
            return True
        return False

    def __lt__(self, obj):
        return not self.__gt__(obj)

    def __str__(self):
        return self.login


def sort(arr, left=0, right=None):
    if not right:
        right = len(arr) - 1
    pivot = arr[randint(left, right)]
    l_ptr = left
    r_ptr = right

    while l_ptr <= r_ptr:
        while arr[l_ptr] > pivot and l_ptr < right:
            l_ptr += 1
        while pivot > arr[r_ptr] and r_ptr > left:
            r_ptr -= 1

        if l_ptr <= r_ptr:
            arr[l_ptr], arr[r_ptr] = arr[r_ptr], arr[l_ptr]
            l_ptr += 1
            r_ptr -= 1

    if r_ptr > left:
        sort(arr, left, r_ptr)
    if l_ptr < right:
        sort(arr, l_ptr, right)


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        login, p, f = input().split()
        arr.append(Member(login, int(p), int(f)))

    sort(arr)
    for user in arr:
        print(user)


if __name__ == '__main__':
    main()
