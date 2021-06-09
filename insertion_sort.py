# insertion_sort


def insertion_sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and item < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item
        # print(f'step {i}, sorted {i+1} elements: {array}')
    return array

assert insertion_sort([11, 2, 9, 7, 1]) == [1, 2, 7, 9, 11]
