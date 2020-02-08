def lcs(x, y):
    short, long = sorted((x, y), key=len)
    if len(short) != len(long):
        return each(short, long)
    else:
        return max((each(short, long), each(long, short)), key=len)

def each(short, long):
    index = 0
    result = ''
    for c in short:
        left = long[index:]
        if c in left:
            result += c
            index += left.find(c) + 1
    return result
