def solution(x, y):
    x = int(x)
    y = int(y)
    count = 0
    while x > 1 and y > 1:
        if x < y:
            count += y // x
            y -= x * (y // x)
        else:
            count += x // y
            x -= y * (x // y)
    if x < 1 or y < 1:
        return "impossible"
    return repr(count + x + y - 2)

