def solution(numbers):
    if numbers == [0] * len(numbers):
        return '0'
    strList = list(map(str, numbers))
    strList.sort(key=lambda x : x * 3, reverse=True)
    return ''.join(strList)

import functools
def answer(numbers):
    def compare(a, b):
        t1 = a + b
        t2 = b + a
        return (int(t1) > int(t2)) - (int(t1) < int(t2))
    n = [str(x) for x in numbers]
    n.sort(key=functools.cmp_to_key(compare), reverse=True)
    return str(int(''.join(n)))


if __name__ == '__main__':
    print(solution([6,10,2]))
    print(answer([6,10,2]))