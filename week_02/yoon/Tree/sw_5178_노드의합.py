class Tree:
    def __init__(self, n):
        self.tree = [0] * (n+1)
        self.size = n

    def setNode(self, node, data):
        self.tree[node] = data

    def sumLeaf(self, node):
        if node * 2 > n:        # n: 노드 수
            self.sum += self.tree[node]
        else:
            self.sumLeaf(node * 2)   # search left node 
            if node * 2 != n:
                self.sumLeaf(node * 2 + 1)   # search right node

    def answer(self, x):
        self.sum  = 0
        self.sumLeaf(x)
        return self.sum


T = int(input())
for test_case in range(1, T+1):
    n, m, l = map(int, input().split())     # n: 노드 수  m: leaf 수  l: target node
    tree = Tree(n)
    for _ in range(m):
        num1, num2 = map(int, input().split())
        tree.setNode(num1, num2)

    print(f"#{test_case} {tree.answer(l)}")