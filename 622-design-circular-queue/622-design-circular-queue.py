class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.cap = k
        self.N = 0
        self.initialize()

    def initialize(self):
        self.head = Node(-1)
        self.rear = self.front = self.head

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear.next = Node(value)
            self.rear = self.rear.next
            
            if self.front.val == -1:
                self.front = self.front.next
            
            self.N += 1
            return 1
  
    def deQueue(self) -> bool:
        if not self.isEmpty():
            f = self.front
            self.front = f.next
            del f
            
            self.N -= 1
            if self.N == 0:
                self.initialize()
            return 1
      
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.front.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        return self.N == 0

    def isFull(self) -> bool:
        return self.cap == self.N 