def merge_sort(array):
    if len(array) == 1:
        return array

    left = merge_sort(array[0:len(array)//2])
    right = merge_sort(array[len(array)//2:len(array)])
    l, r, k = 0, 0, 0
    result = [None] * len(array)

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

def search(sub_seq, text):
    if len(sub_seq) > len(text):
        return False

    k = 0
    i = 0
    
    while k < len(text):
        if i == len(sub_seq) - 1:
            return True
        if text[k] == sub_seq[i]:
            i += 1
        k += 1
    return False


def main():
    assert search('abcp', 'ahpc') == False
    assert search('islx','yoytgtshldmogkdburkbcfvoapepjpcuwemusfkfztrzxstytrnarlizjhuoscuzlraezlaweipuuqdgvhwkhhoufexojaps') == True
    sub_seq = input()
    text = input()

    print(search(sub_seq, text))

if __name__ == '__main__':
    main()
