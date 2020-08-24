from collections import Counter
# from functools import reduce
def solution(clothes):
    answer = 1
    cloth_dict = Counter([y for x, y in clothes])           # clothes input에서 의상의 종류만 리스트에 담아서
                                                            # Counter함수로 종류 별 갯수 확인
    for i in cloth_dict.values():
        answer *= (i + 1)
    # answer = reduce(lambda x, y : x * (y + 1), cloth_dict.values(), 1)    # 위의 두줄 reduce로 표현
    return answer - 1



a = [1,1,1,2,3,1,2,3,4]
print(Counter(a))