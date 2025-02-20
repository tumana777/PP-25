#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#
#         if not self.head:
#             self.head = new_node
#             return
#
#         current = self.head
#
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def delete(self, data):
#         current = self.head
#
#         if current and current.data == data:
#             self.head = current.next
#             current = None
#             return
#
#         prev = None
#
#         while current and current.data != data:
#             prev = current
#             current = current.next
#
#         if current is None:
#             return
#
#         prev.next = current.next
#         current = None
#
#     def print_list(self):
#         current = self.head
#
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#
# ll = LinkedList()
# ll.append(4)
# ll.append(3)
# ll.append(6)
# ll.append(5)
#
# ll.prepend(2)
# ll.prepend(7)
#
# # ll.print_list()
#
# ll.delete(2)
# ll.delete(6)
#
# ll.print_list()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def empty(self):
#         return self.size == 0
#
#     def peek(self):
#         if self.empty():
#             return "Stack is empty"
#         return self.top.data
#
#     def push(self, data):
#         new_node = Node(data)
#
#         new_node.next = self.top
#         self.top = new_node
#         self.size += 1
#
#     def pop(self):
#
#         if self.empty():
#             return "Stack is empty"
#
#         popped_element = self.top.data
#
#         self.top = self.top.next
#         self.size -= 1
#         return popped_element
#
# stack = Stack()
#
# # print(stack.empty())
#
# stack.push(5)
# stack.push(6)
# # print(stack.peek())
# stack.push(8)
# stack.push(9)
# # print(stack.peek())
# stack.push(2)
# stack.push(6)
# stack.push(1)

# print(stack.peek())
# x = stack.pop()
# stack.pop()
# popped = stack.pop()
# #
# # print(stack.peek())
# # print(popped)
#
# print(stack.size)

