import string

def moveLR(name, direction='right'):
    idx   = 0
    name  = list(name)
    count = -1                                                          # 맨 마지막에서 한번더 +1 되니까 -1에서 시작
    while "".join(name) != 'A'*len(name):
        if name[idx] != "A":                                            # "A"가 아니면 A로 바꾼다
            name[idx] = "A"
        count += 1
        idx = idx + (1 if direction == 'right' else -1)                 # direction이 left면 index -1씩 더한다
    return count                                                        # 좌 or 우로 이동하는 횟수 return

def solution(name):
    alpha = string.ascii_uppercase
    answer = 0

    for ch in name:
        idxR = alpha.index(ch)                                          # 알파벳 string에서 몇 번째 index에 있는지 == 위로 이동한횟수
        idxL = 26 - idxR                                                # 전체 26에서 위로 이동만큼 빼면 아래로 이동한 횟수
        moveUD = min(idxR, idxL)                                        # 위, 아래 중 작은 수를 더한다
        answer += moveUD
    directionR, directionL = moveLR(name), moveLR(name, 'left')         

    answer += min(directionR, directionL)                               # moveLR의 결과 중 작은수 더한다
    return answer

#print(solution("ABAAAAAAAAABB"))
print(solution("JEROEN"))
print(solution("JAN"))
