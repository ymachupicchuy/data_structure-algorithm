class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def isInList(head, node):
    current = head
    while current:
        if current.value == node.value:
            return True
        current = current.next
    return False


def union(llist_1, llist_2):
        # Your Solution Here
        if llist_1.size() == 0 or llist_2.size() == 0:
            return 'Empty'

        llList = LinkedList()
        hashSet = set()
        current1 = llist_1.head
        current2 = llist_2.head

        while current1:
            if current1.value not in hashSet:
                hashSet.add(current1.value)
            current1 = current1.next
     
        while current2:
            if current2.value not in hashSet:
                hashSet.add(current2.value)
            current2 = current2.next
        
        for key in hashSet:
            llList.append(key)
        return llList

def intersection(llist_1, llist_2):
    if llist_1.size() == 0 or llist_2.size() == 0:
        return 'Empty'
    llList = LinkedList()
    hashSet = set()
    current1 = llist_1.head
    current2 = llist_2.head

    while current1:
        if current1.value not in hashSet:
            hashSet.add(current1.value)
        current1 = current1.next

    while current2:
        if current2.value in hashSet:
            llList.append(current2.value)
        current2 = current2.next
    return llList


#Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]


for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

def test3():
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    return union(linked_list_5,linked_list_6)

print(test3() == 'Empty')
# True


# Test case 5

def test4():
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = []
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_7.append(i)

    for i in element_2:
        linked_list_8.append(i)

    return intersection(linked_list_7,linked_list_8)

print(test4() == 'Empty')
# True
    
