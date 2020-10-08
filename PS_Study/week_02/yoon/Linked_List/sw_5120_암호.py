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
        self.tail = new_node                    # 새 노드를 기존 tail과 연결시켜 tail갱신
        self.tail.link = self.head.link         # 원형연결리스트이므로 tail과 head연결
        self.size += 1

    def get_first(self):
        self.current = self.head.link           # 첫 번째 노드 --> head와 연결된 것.
        self.before = self.tail                 # 원형연결리스트에서 첫 노드의 이전것이 tail
        return self.current.data

    def get_next(self):                         # 다음 노드 이동시키는 메소드
        self.before = self.current
        self.current = self.current.link 
        return self.current.data

    def insert_node(self, data):
        new_node = Node(data)
        new_node.link = self.current            # 현재 노드를 새 노드 다음에 연결
        self.before.link = new_node             # before.link --> get_next로 이동시켰기 때문에 before다음에 삽입해야함 ( befor --> new --> current )
        self.current = new_node                 # 새 노드를 현재 노드로
        self.size += 1

    def task(self, step):
        for _ in range(step):                   # M만큼 이동해서 새 노드 삽입
            self.get_next()
        num = self.before.data + self.current.data  # 새 노드의 data는 앞뒤 데이터의 합 / 원형연결리스트이므로 자동으로 다음이 없으면 맨앞것 불러옴
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


        
    