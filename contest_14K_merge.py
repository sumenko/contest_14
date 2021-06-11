# 14 Спринт
# K. Сортировка слиянием

def merge(left, right):
    l, r, k = 0, 0, 0
    result = [None] * (len(left) + len(right))

    while l < len(left) and r < len(right):
        # print(k, l, r)
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result


def merge_sort(array):
    if len(array) == 1:
        return array

    left = merge_sort(array[0:len(array)//2])
    print('left', left)
    right = merge_sort(array[len(array)//2:len(array)])
    print('right', right)
    return merge(left, right)



assert merge_sort([1, 5, 3, 2, 4]) == [1, 2, 3, 4, 5]
assert merge_sort([10, 5, 5, 2, 4]) == [2, 4, 5, 5, 10]
