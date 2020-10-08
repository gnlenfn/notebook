import sys

sys.stdin=open('sample_input5102.txt','r')

############################수정필요##############################

def make_graph(v,e):
    
    graph={i+1:[] for i in range(v)}

    for _ in range(e):
        
        start_vertex,target_vertex=map(int,input().split())
        
        graph[start_vertex].append(target_vertex)
        graph[target_vertex].append(start_vertex) #양방향그래프
        
    return graph

def BFS(s,e,graph):

    explore.append(s)
    #print("explore",explore)

    count=0
    
    while explore:
        
        vertex=explore.pop(0)
        
        if e in graph[vertex]:
            count+=1
            break

        if vertex not in visit:

            count+=1

            visit.append(vertex)
            explore.extend(graph[vertex])

            #print("visit",visit)
            #print("explore",explore)
            
    return count
            
        
T=int(input())

for test_case in range(1,T+1):
    
    V,E=map(int,input().split())

    Graph=make_graph(V,E)
    #print(Graph)

    explore=[]
    visit=[]

    S,G=map(int,input().split())

    print('#{} {}'.format(test_case,BFS(S,G,Graph)))
