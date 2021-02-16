def panlindrome(data):
    if len(data) <= 1:
        return True
    elif len(data) > 1:
        if data[0] == data[-1]:
            return panlindrome(data[1:-1])
        else:
            return False

print(panlindrome('ppapp'))
print(panlindrome('raser'))
print(panlindrome('asdffdsa'))