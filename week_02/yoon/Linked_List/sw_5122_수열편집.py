class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node

        self.before = None
        self.current = None
        self.size = 0

    def append(self, data):                     # 수열 input대로 노드 생성
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node
        self.size += 1

    def move(self, step):                       # 주어진 index로 이동시키는 메소드
        self.current = self.head.link
        self.before = self.head
        for _ in range(step):
            if self.current == None:
                return False
            self.before = self.current
            self.current = self.current.link 
        return True

    def insert(self, idx, data):                # move(idx) 후 그자리에 새 노드 삽입
        new_node = Node(data)
        self.move(idx)
        self.before.link = new_node
        new_node.link = self.current
        self.size += 1

    def delete(self, idx):                      # move(idx) 후 해당 노드 삭제
        self.move(idx)
        self.before.link = self.current.link 

    def change(self, idx, data):                # move(idx) 후 해당 노드 data 교체
        self.move(idx)
        self.current.data = data

    def printResult(self, idx):
        if self.move(idx):                      # l만큼 이동하면, 해당 노드 data 출력
            return self.current.data 
        else:                                   # l이 없으면
            return -1

T = int(input())
for test_case in range(1, T+1):
    n, m, l = map(int, input().split())
    seq = LinkedList()
    for i in map(int, input().split()):         # 수열 input  
        seq.append(i)

    for _ in range(m):
        task = list(input().split())
        if task[0] == 'I':
            seq.insert(int(task[1]), int(task[2]))
        elif task[0] == 'D':
            seq.delete(int(task[1]))
        elif task[0] == 'C':
            seq.change(int(task[1]), int(task[2]))

    
    # answer = seq.printResult(l)
    print(f'#{test_case} {answer}')
