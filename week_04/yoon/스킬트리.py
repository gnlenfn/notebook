def solution(skill, skill_trees):
    answer = 0
    while skill_trees:                          # skill_trees가 빌 때 까지
        flag = False
        tree = skill_trees.pop(0)               # 첫 번째 스킬트리 pop
        stack = []
        for i in tree:
            if i in skill:                      # 스킬트리에 영향을 받으면 append
                stack.append(i)                 # 아니면 pass해도 무관
        if stack:                  
            if "".join(stack) == skill[:len(stack)]: # 스킬트리와 일치하는지 확인
                flag = True
                answer += 1
        else:                                   # stack이 비었으면 스킬트리에
            flag = True                         # 영향받는 스킬 안찍은 것
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))