# linked list head and tail
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self,ele):
        if self.head is None:
            self.head = self.tail = Node(ele)
        else:
            newnode = Node(ele)
            self.tail.next = newnode
            self.tail = newnode
    def pop(self):
        temp = self.head
        self.head = self.head.next
        print("element poped is ",temp.data)
    def print(self):
        temp = self.head
        while(temp.next!=None):
            print(temp.data,end="->")
            temp = temp.next
        print(temp.data)
    def atbegin(self,ele):
        newnode = Node(ele)
        newnode.next = self.head
        self.head = newnode
    def atposition(self,n,ele):
        newnode = Node(ele)
        if self.head is None:
            newnode.next = self.head=self.tail
            self.head = self.tail = newnode
        else:
            temp = self.head
            for i in range(1,n-1):
                if temp!=None:
                    temp = temp.next
            newnode.next=temp.next
            temp.next=newnode
    def del_dup(self):
        previous = None
        current = self.head
        s = set()
        while current:
            if current.data in s:
                previous.next = current.next
            else:
                s.add(current.data)
                previous = current
            current = previous.next
    def reverse(self):
        previous = None
        current = self.head
        curnext = None
        while current!=None:
            curnext = current.next
            current.next = previous
            previous = current
            #curnext.next = previous
            current = curnext
        self.head = previous
    def delposition(self,n):
        temp = self.head
        for i in range(1,n-1):
            if temp!= None:
                temp = temp.next
        temp.next = temp.next.next
    def sortlist(self):
        current = self.head
        curnext = None
        while current!=None:
            curnext = current.next
            while curnext!=None:
                if current.data > curnext.data:
                    temp = current.data
                    current.data = curnext.data
                    curnext.data = temp
                curnext = curnext.next
            current = current.next
ob = Linkedlist()
ob.push(10)
ob.push(20)
ob.push(30)
ob.push(40)
ob.push(20)
ob.print()
ob.atbegin(100)
ob.print()
ob.atposition(3,100)
ob.print()
ob.del_dup()
ob.print()
ob.delposition(3)
ob.print()
ob.sortlist()
ob.print()
ob.reverse()
ob.print()
