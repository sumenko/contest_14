from random import randrange

def partition(array, pivot):
    less = [i for i in array if i < pivot]
    center = [i for i in array if i == pivot]
    greater = [i for i in array if i > pivot]
    return less, center, greater

def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = randrange(len(array))
    less, center, greater = partition(array, pivot)
    return quick_sort(less) + center + quick_sort(greater)

if __name__ == '__main__':
    array = [5, 5, 5, 5, 4, 3, 2, 2, 2, 2, 1]
    less, center, greater = partition(array, 3)
    print(less, center, greater)

    print(quick_sort(array))
