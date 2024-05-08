# class Queue:
#     queue = []

#     def push(self, item):
#         self.queue.append(item)

#     def pop(self):
#         return self.queue.pop(0)

#     def is_empty(self):
#         return self.queue == []


# class Node:
#     def __init__(self, item) -> None:
#         self.item = item
#         self.next = None


# class Queue:
#     def __init__(self) -> None:
#         self.head = self.tail = None

#     def push(self, item):
#         new_node = Node(item)
#         if self.is_empty():
#             self.head = new_node
#             self.tail = self.head
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#     def pop(self):
#         if self.is_empty():
#             return None
#         temp = self.head.item
#         self.head = self.head.next
#         return temp

#     def is_empty(self):
#         return self.head is None