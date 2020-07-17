import sys

sys.stdin = open("sample_input4871.txt", "r")
def make_graph(v,e): #vertex edge

    #vertex들간의 관계를 지어주는 딕셔너리 생성
    graph={i+1:[] for i in range(v)}

    for _ in range(e):
        start_vertex,target_vertex=map(int,input().split())
        graph[start_vertex].append(target_vertex)
    return graph
        
def DFS(s,e,graph): #start_vertex end_vertex graph

    explore.append(s)

    arrival=0

    #경로탐색 시작 
    while explore:
        
        vertex=explore.pop()
        
        if vertex==e:
            arrival=1
            break

        if vertex not in visit:
            visit.append(vertex)
            explore.extend(graph[vertex]) #방문할 다음 vertex들을 저장
            print(explore)
            
    return arrival
    

T = int(input())

for test_case in range(1,T+1):
    
    V,E=map(int,input().split())

    Graph=make_graph(V,E)

    explore=[]
    visit=[]

    S,G=map(int,input().split())

    print('#{} {}'.format(test_case,DFS(S,G,Graph)))
