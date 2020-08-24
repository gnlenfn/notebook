def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        leng = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if phone_book[j][:leng] == phone_book[i]:
                answer = False
                break
        
    return answer
####### 효율성 탈락 #########


import re
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        start = '^' + phone_book[i] 
        for j in range(i + 1, len(phone_book)):
            if re.match(start, phone_book[j]):
                return False
    return True




# 다른 사람의 풀이
def solution(phone_book):
    phone_book.sort()
    for i, j in zip(phone_book, phone_book[1:]):    # 기존 리스트와 현재보는 번호 다음 것 부터 시작하는 문자열 zip으로 묶어
        if j.startswith(i):                         # startswith methon --> 주어진 문자열로 시작하는지 확인
            return False
    return True