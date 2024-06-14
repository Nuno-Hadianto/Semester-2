#stack
class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL :
    def __init__(self):
        self.top = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push (self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size +=1
    
    def pop (self):
        if self.is_empty():
            return None
        pop_item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return pop_item
    
    def peek (self) :
        if self.is_empty():
            return None
        return self.top.data
    
    def size(self) :
        return self.size
    
    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
stack = StackLL()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

stack.display()
print ("Elemen teratas", stack.peek())
print ("Size Stack", stack.size)

pop_itm = stack.pop()
print("Elemen dihapus", pop_itm)
print ("Elemen teratas", stack.peek())
print ("Size Stack", stack.size)


#queue
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class QueueLL:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self._size = 0
    
#     def is_empty(self):
#         return self._size == 0
    
#     def enqueue(self, item):
#         new_node = Node(item)
#         if self.is_empty():
#             self.front = new_node
#             self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#         self._size += 1
    
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         dequeue_item = self.front.data
#         if self.front == self.rear:
#             self.front = None
#             self.rear = None
#         else:
#             self.front = self.front.next
#         self._size -= 1
#         return dequeue_item
    
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.front.data
    
#     def size(self):
#         return self._size
    
#     def display(self):
#         current = self.front
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()


# queue = QueueLL()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)

# queue.display()

# print("Elemen di depan antrian:", queue.peek())
# print("Ukuran Antrian:", queue.size())

# dequeue_item = queue.dequeue()
# print("Elemen yang dihapus:", dequeue_item)

# print("Elemen di depan antrian:", queue.peek())
# print("Ukuran Antrian:", queue.size())