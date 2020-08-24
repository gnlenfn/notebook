import math

def solution(w,h):
    r = math.gcd(w, h)        # 가로,세로 최대공약수
    a, b = w / r, h / r       # 최소단위 사각형의 가로, 세로
    rec = a + b - 1           # 최소단위 사각형에서 잘린 사각형의 수   
    flaw = int(rec * w / a)   # 잘린 사각형 수
    return w * h - flaw

print(solution(8,12))