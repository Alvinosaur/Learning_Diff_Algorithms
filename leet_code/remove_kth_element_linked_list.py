class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
    # Fill this in.
    if head is None: return None  # not enough nodes to reach kth
    if k == 0: return head.next
    head.next = remove_kth_from_linked_list(head.next, k-1)
    return head
  
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]