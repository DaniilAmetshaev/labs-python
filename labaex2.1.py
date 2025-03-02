def close(s):
    if not s:
        return ""

    kollich = []
    count = 1
    length = len(s)

    for i in range(1, length):
        if s[i] == s[i - 1]:
            count += 1
        else:
            kollich.append(s[i - 1])
            if count > 1:
                kollich.append(str(count))
            count = 1
            
    kollich.append(s[-1])
    if count > 1:
        kollich.append(str(count))

    return ''.join(kollich)

inputstr = "YYYYggkeeeAAABV"
closestr = close(inputstr)
print(closestr)  