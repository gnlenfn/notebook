import sys
sys.stdin=open('sample_input5097.txt','r')

T = int(input())

for test_case in range(1, T + 1):

    N,M = map(int, input().split())
    nums=list(map(int, input().split()))
    
    #print(nums)
    
    for i in range(M): #M번만큼 이동
        nums.append(nums.pop(0)) #FIFO
    print('#{0} {1}'.format(test_case,nums[0]))
