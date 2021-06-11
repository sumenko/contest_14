def search(sub, text):
    """ поиск вперед """
    if len(sub) > len(text):
        return False
    k = 0
    i = 0
    while k < len(text):
        if i == len(sub):
            return True
        if text[k] == sub[i]:
            i += 1
        k += 1
    return i == len(sub)


def search2(sub, text):
    """ поиск назад """
    if sub == '':
        return True
    i = len(sub) - 1
    for c in text[::-1]:
        if i < 0:
            return True
        if c == sub[i]:
            i -= 1
    return i < 0


def main():
    assert search('abc', 'ahbgdcu') == True
    assert search('abcp', 'ahpc') == False
    assert search('islx','yoytgtshldmogkdburkbcfvoapepjpcuwemusfkfztrzxstytrnarlizjhuoscuzlraezlaweipuuqdgvhwkhhoufexojaps') == True
    assert search('6','ggzj') == False
    sub_seq = input()
    text = input()

if __name__ == '__main__':
    main()
