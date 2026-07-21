class Node:
    def __init__(self,key,value):
        self.prev=None
        self.key=key
        self.value=value
        self.nextt=None

class DoubleLinkedList:
    def __init__(self):
        self.head=Node(1,1)
        self.tail=Node(1,1)
        
        self.head.nextt=self.tail
        self.tail.prev=self.head
    
    def add_node(self,node):
        nextt=self.head.nextt

        self.head.nextt=node
        node.prev=self.head

        node.nextt=nextt
        nextt.prev=node
    
    def remove_node(self,node):
        prev=node.prev
        nextt=node.nextt

        nextt.prev=prev
        prev.nextt=nextt


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hash={}
        self.dll=DoubleLinkedList()
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        else:
            node=self.hash[key]
            self.dll.remove_node(node)
            self.dll.add_node(node)

            return node.value
        

    def put(self, key: int, value: int) -> None:

        if key not in self.hash:
            if len(self.hash)==self.capacity:
                to_be_removed=self.dll.tail.prev
                self.dll.remove_node(to_be_removed)
                del self.hash[to_be_removed.key]
            node=Node(key,value)
            self.hash[key]=node
            self.dll.add_node(node)
        else:
            node=self.hash[key]
            node.value=value
            self.dll.remove_node(node)
            self.dll.add_node(node)
        
        
        
        



            





        
