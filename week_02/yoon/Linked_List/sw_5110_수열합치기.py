class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


"""
현재 노드 --> (self.data, self.link)
data는 현재 노드의 값
link는 이전 노드의 주소 
"""
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
        self.tail.link = new_node           # tail에 새로운 노드를 연결
        self.tail = new_node                # tail 갱신
        self.size += 1                      # 리스트 사이즈 +1

    def first(self):
        if self.size == 0:
            return None                     # 맨앞에 삽입
        self.before = self.head             # before를 head로 --> 맨앞에 놓는 다는 뜻
        self.current = self.head.link       # 현재 노드를 head에 연결
        return self.current.data            # 현재 수열의 첫 번째 값을 return

    def next(self):
        self.before = self.current          # current를 before로
        self.current = self.current.link    # 주소 연결
        if self.current == None:
            return None
        return self.current.data

    def insert_list(self, new_list):
        # 문제에서 말하는 첫 숫자보다 큰 숫자를 찾아 삽입
        insert_num = new_list.first()       
        num = self.first()                  # 삽입할 수열의 첫 번째 수
        flag = 0
        for _ in range(self.size):
            if num > insert_num:            # 기존 수열의 수가 새로운 수열의 첫 번째 수보다 크다면
                self.before.link = new_list.head.link  # 이전 노드를 새 수열의 헤드와 연결
                new_list.tail.link = self.current      # 현재 노드를 새 수열의 tail과 연결
                self.size += new_list.size
                flag = 1
                break
            num = self.next()               # 크지 않으면 다음 노드로 이동
        
        # 기존 수열에 큰 수가 없으면
        if flag == 0:
            self.tail.link = new_list.head.link 
            self.size += new_list.size

    def print_result(self):
        result = []
        num = self.first()
        for i in range(self.size):          # 만들어진 전체 수열을 리스트에 append
            result.append(num)
            num = self.next()
        return " ".join(map(str, result[-1:-11:-1]))  # 맨 뒤에서 10개 출력
  
T = int(input())

for test_case in range(1, T+1):
    n, m = map(int,input().split())
    seq = LinkedList()
    for i in map(int, input().split()):
        seq.append(i)

    for _ in range(m-1):
        seq2 = LinkedList()
        for j in map(int, input().split()):
            seq2.append(j)

        seq.insert_list(seq2)

    print(f'#{test_case} {seq.print_result()}')
