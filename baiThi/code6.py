"""Viết chương trình đảo 1 danh sách liên kết



Output mẫu:

Given Linked List
12 43 8 95
Reversed Linked List
95 8 43 12"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def them_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def dao_danh_sach(self):
        if self.head:
            self.head = self.reverse(self.head)

    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def in_danh_sach(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

linked_list = LinkedList()
n = int(input("nhap so luong phan tu cua list: "))
for i in range(n):
    m = int(input("them: "))
    linked_list.them_node(m)


print("Given Linked List")
linked_list.in_danh_sach()

linked_list.dao_danh_sach()

print("Reversed Linked List")
linked_list.in_danh_sach()

