class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    """Given the root of a tree of Nodes, return a string that represents this
    tree. String should be reversible by the deserialize() function.
    """
    if not node: return 'None'
    res = node.val + ','
    res += serialize(node.left) + ','
    res += serialize(node.right)
    return res

def deserialize(node_str):
    vals = node_str.split(',')
    vals.reverse()
    return deserialize_helper(vals)

def deserialize_helper(list_node_str):
    val = list_node_str.pop()
    if val == 'None': return None
    root = Node(val)
    root.left = deserialize_helper(list_node_str)
    root.right = deserialize_helper(list_node_str)
    return root

def test():
    A = (Node('A', Node('B', Node('D', None, Node('F')), Node('E')), 
                   Node('C', None, Node('F'))))
    print(serialize(A))
    print(serialize(deserialize(serialize(A))))

test()