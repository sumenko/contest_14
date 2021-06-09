# Спринт 14
# B. Комбинации

kbd = {
    '2': 'abc', '3': 'def',
    '4': 'ghi', '5': 'jkl', '6': 'mno',
    '7': 'pqrs','8': 'tuv', '9': 'wxyz'
}


def generator(numbers, collection, txt='', idx=0):
    if idx == len(numbers):
        collection.append(txt)
        return
    seq = kbd[numbers[idx]]
    for ch in seq:
        generator(numbers, collection, txt + ch, idx + 1)


def main():
    collection = []
    generator(input(), collection)
    print(*collection)


if __name__ == '__main__':
    main()
