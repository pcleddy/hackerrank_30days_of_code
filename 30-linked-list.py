class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        #print(head, data)
        new_node = Node(data)
        if not head:
            head = new_node
        else:
            current = head
            while current:
                if current.next:
                    current = current.next
                else:
                    current.next = new_node
                    break
        return head


mylist = Solution()

T = int(input())

head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head);
