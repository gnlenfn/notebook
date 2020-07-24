class Tree:
    def __init__(self):
        self.heap = [0]

    def sort(self, num):
        if num >= 2:
            if self.heap[num] < self.heap[num // 2]:
                self.heap[num], self.heap[num // 2] = self.heap[num // 2], self.heap[num]
                self.sort(num // 2)

    def append(self, data):
        num = len(self.heap)
        self.heap.append(data)
        self.sort(num)

    def makeSum(self, node):
        if node <= 1:
            return self.heap[node]
        else:
            return self.heap[node] + self.makeSum(node // 2)

    def getAnswer(self):
        idxLast = len(self.heap) - 1
        self.sum = 0
        if idxLast >= 2:
            return self.makeSum(idxLast // 2)
        else:
            return 0

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    h = Tree(n)
    data = list(map(int, input().split()))
    for i in range(n):
        h.append(data[i])

    #print(f"#{test_case} {h.getAnswer()}")