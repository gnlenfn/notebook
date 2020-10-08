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

#####완전이진트리#####

class BST:
    def __init__(self,n):
        self.tree=[0]*(n+1)
        self.n=n
        self.value=1
        self.insert(1)

    def insert(self,index): #recursive manner
        if index<=self.n: 
            self.insert(index*2) #explore left subtree
            
            self.tree[index]=self.value
            self.value+=1
            
            self.insert(index*2+1) #explore right subtree

            #order: left -> middle -> right

    def return_value(self):
        root_node=self.tree[1]
        target_node=self.tree[self.n//2]
        return root_node, target_node
        
T=int(input())

for test_case in range(1,T+1):
    N=int(input())
    
    tree=BST(N)

    Root,Target=tree.return_value()
    print('#{} {} {}'.format(test_case,Root,Target))

