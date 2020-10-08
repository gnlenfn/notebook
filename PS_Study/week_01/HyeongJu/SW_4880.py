import sys

sys.stdin=open('sample_input4880.txt','r')

#1=가위 2=바위 3=보
def card_game(left,right):

    #숫자가 같으면 왼쪽 승
    if student_list[left-1]==student_list[right-1]:
        return left

    #왼쪽이 이기는 경우
    elif student_list[left-1]==1 and student_list[right-1]==3:
        return left

    elif student_list[left-1]==2 and student_list[right-1]==1:
        return left

    elif student_list[left-1]==3 and student_list[right-1]==2:
        return left
    
    #오른쪽이 이기는 경우
    else:
        return right
    
def tournament(start,end):
    if start==end:
        return start #group change
    left_group=tournament(start,(start+end)//2)
    right_group=tournament((start+end)//2+1,end)
    #print("left",left_group)
    #print("right",right_group)
    return card_game(left_group,right_group)



T=int(input())

for test_case in range(1,T+1):
    
    N=int(input())
    
    i,j=1,N
    
    student_list=list(map(int,input().split()))

    print('#{} {}'.format(test_case,tournament(i,j)))
