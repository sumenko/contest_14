def as_binary_string(n):
    if n < 0:
        return '-' + as_binary_string(-n)
    if n == 0 or n == 1:
        return str(n)
    last_digit = n % 2
    return as_binary_string(n // 2) + str(last_digit)


print(as_binary_string(128))
print(as_binary_string(127))
print(as_binary_string(7))
print(as_binary_string(0))
print(as_binary_string(1))
print(as_binary_string(2))
