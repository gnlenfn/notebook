import sys

sys.stdin = open("sample_input4869.txt", "r")

#Dynamic Programming

def paste_paper(n):
    result_list=[]

    result_list.append(1)
    result_list.append(3)

    if n==10:
        return 1

    elif n==20:
        return 3
    
    else:
        for i in range(2,n//10):
            result=result_list[i-1]+result_list[i-2]*2 #점화식
            result_list.append(result)

        return result

    
T = int(input())

for test_case in range(1,T+1):
    N=int(input())
    print("#{0} {1}".format(test_case,paste_paper(N)))

    
