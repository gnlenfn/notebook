import sys

sys.stdin=open('sample_input5176.txt','r')
'''
#####완전이진트리x#####
class Node:
    def __init__(self,data,left_child=None,right_child=None):
        self.data=data
        self.left_child=left_child
        self.right_child=right_child

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.insert_node(data,self.root)

    def insert_node(self,data,node):

        #left subtree

        if data<node.data:
            if node.left_child!=None:
                self.insert_node(data,node.left_child)
            else:
                node.left_child=Node(data)

        #right subtree

        elif data>node.data:
            if node.right_child!=None:
                self.insert_node(data,node.right_child)
            else:
                node.right_child=Node(data)

    def preorder(self):
        def preorder(root):
            print(root.data,end=' ')
            if root!=None:
                if root.left_child!=None:
                    preorder(root.left_child)

                if root.right_child!=None:
                    preorder(root.right_child)
        preorder(self.root)

        print()
            
'''

        
T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    
    tree=BST(N)

