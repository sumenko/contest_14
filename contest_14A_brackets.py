# Спринт 14
# A. Генератор скобок

def is_correct_bracket_seq(seq: str) -> bool:
    closed_bracket = {
        '(': ')',
    }
    stack = []
    if seq == '':
        return True
    if not seq[0] in closed_bracket.keys():
        return False
    stack.append(seq[0])
    for c in seq[1:]:
        if (stack != [] and
           stack[-1] in closed_bracket.keys() and
           closed_bracket[stack[-1]] == c):
            stack.pop()
            continue
        stack.append(c)
    return stack == []


def brackets(n, pref):
    if n == 0:
        if pref[0] == '(':
            if is_correct_bracket_seq(pref):
                print(pref)
        return pref
    else:
        n = n - 1
        for b in ('(', ')'):
            brackets(n, pref + b)



def main():
    n = int(input())
    brackets(n * 2, '')


if __name__ == '__main__':
    main()
