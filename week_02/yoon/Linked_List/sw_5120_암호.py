# 원형연결리스트 이용

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None # 다음 노드의 주소

class LinkedList:
    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node

        self.before = None
        self.current = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node
        self.tail.link = self.head.link
        self.size += 1

    def get_first(self):
        self.current = self.head.link
        self.before = self.tail
        return self.current.data

    def get_next(self):
        self.before = self.current
        self.current = self.current.link 
        return self.current.data

    def insert_node(self, data):
        new_node = Node(data)
        self.before.link = new_node
        new_node.link = self.current
        self.current = new_node
        self.size += 1

    def task(self, step):
        for _ in range(step):
            self.get_next()
        num = self.before.data + self.current.data 
        self.insert_node(num)

    def get_result(self):
        result = [self.get_first()]
        for _ in range(self.size - 1):
            result.append(self.get_next())

        return ' '.join(map(str, result[-1:-11:-1]))

T = int(input())
for test_case in range(1, T+1):
    n, m, k = map(int, input().split())                 # N, M, K 입력
    seq = LinkedList()
    for i in map(int, input().split()):                 # 리스트값 입력
        seq.append(i)
    seq.get_first()
    for _ in range(k):                                  # M칸 이동하여 노드추가를 K만큼 반복
        seq.task(m)
    
    answer = seq.get_result()
    print(f'#{test_case} {answer}')


        
    