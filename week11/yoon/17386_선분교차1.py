def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

line1 = list(map(int, input().split()))
a, b = (line1[0], line1[1]), (line1[2], line1[3])

line2 = list(map(int, input().split()))
c, d = (line2[0], line2[1]), (line2[2], line2[3])

if ccw(a, b, c) * ccw(a, b, d) < 0 and ccw(c, d, a) * ccw(c, d, b) < 0:
    print(1)
else:
    print(0)