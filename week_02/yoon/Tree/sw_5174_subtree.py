class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class Tree:
    def __init__(self):
        self.root = None
        self.nodeList = [self.root]
        for i in range(e+1):            # node 번호는 1부터 e+1 총 e개
            self.nodeList.append(Node(i))

    def insert(self, parent, child):
        if self.nodeList[parent].left == None:
            self.nodeList[parent].left = self.nodeList[child]
        else:
            self.nodeList[parent].right = self.nodeList[child]

    def countNodes(self, node):         # 재귀를 통해 subtree 노드 수 세기
        self.count += 1
        if node.left != None:
            self.countNodes(node.left)
        if node.right != None:
            self.countNodes(node.right)

    def printResult(self, num):
        self.count = 0
        self.countNodes(self.nodeList[num])
        return self.count



T = int(input())

for test_case in range(1, T+1):
    e, n = map(int, input().split()) # e: 간선 갯수, n: target 루트 노드
    tree = Tree()
    nums = list(map(int, input().split()))
    for i in range(e):
        tree.insert(nums[2*i], nums[2*i+1])  # tree 생성

    answer = tree.printResult(n)

    print(f"#{test_case} {answer}")
    
