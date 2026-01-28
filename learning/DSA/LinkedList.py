
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next
        print(" ", end="\n")

    def append(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1


    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            print("value of given index is ", temp.value)
        return temp
            
    def setValue(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else: return False

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)
        temp = self.get(index-1)
        newNode = Node(value)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1

    def remove(self,index):
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp =after

        
        

linkedList = LinkedList(3)
linkedList.append(5)
linkedList.append(10)
linkedList.append(15)
# linkedList.pop()
linkedList.prepend(99)
# linkedList.popfirst()
# linkedList.popfirst()
# print(linkedList.get(4))
# linkedList.setValue(1, 55)
# linkedList.insert(2, 45)
# linkedList.remove(5)
linkedList.reverse()
linkedList.printList()

print("length is ", linkedList.length)
