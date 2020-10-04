import re
from itertools import permutations
def solution(expression):
    answer = 0
    expression = re.split("([*+-])", expression)
    cases = permutations(["*", "+", "-"], 3)
    result = []
    for case in cases:
        exp = expression[:]
        for op in case:
            while op in exp:
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1] + exp[idx] + exp[idx+1]))
                del exp[idx:idx+2]
        result.append(abs(int(exp[0])))
    
                
    return max(result)


print(solution("100-200*300-500+20"))