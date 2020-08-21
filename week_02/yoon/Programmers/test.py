from collections import Counter

def solution(no, works):
    s = Counter(works)
    while no > 0:
        dic = sorted(s, reverse=True)
        key_max = dic[0]
        num_max = s[key_max]
        print(num_max, key_max)
        if (key_max - 1) in s:
            print('yes')
            s[key_max - 1] += num_max
        else:
            print('no')
            s[key_max - 1] = num_max
        del s[key_max]
        print(s)
        no -= num_max
        print(no)
    answer = 0
    for i in s.keys():
        answer += i ** 2 * s[i]

    print(answer)

        








print(solution(4, [3,3,3]))
# if "__name__" == "__main__":
#     #print(solution(2, [3,3,3]))