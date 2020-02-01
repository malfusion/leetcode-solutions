"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        node = head
        while(node):
            nextNode = node.next
            node.next = Node(node.val, nextNode, None)
            node = nextNode
        
        node = head
            
        while(node):
            copiedCurr = node.next
            nextNode = copiedCurr.next
            if node.random:
                copiedCurr.random = node.random.next
            if copiedCurr.next:
                copiedCurr.next = copiedCurr.next.next
            node = nextNode
        
        return head.next
            
            
        
    
    
