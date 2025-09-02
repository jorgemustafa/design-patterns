class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.current = None

    # Define Iterator
    def __iter__(self):
        self.current = self.head
        return self

    # Iterate
    def __next__(self):
        if self.current:
            val = self.current.value
            self.current = self.current.next
            return val
        else:
            raise StopIteration

# Initialize LinkedList
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
my_list = LinkedList(head)

# Iterate through LinkedList
for n in my_list:
    print(n)