import queue

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

def bfs(root):
    if root is None: return
    Q = queue.Queue()
    Q.put(root)
    while not Q.empty():
        node = Q.get()
        print(node.val)
        if node.left is not None: Q.put(node.left)
        if node.right is not None: Q.put(node.right)



A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)
A.left,  A.right = B, C
B.left, B.right = D, E
C.right = F
#      A
#    B    C
#   D E    F
bfs(A)