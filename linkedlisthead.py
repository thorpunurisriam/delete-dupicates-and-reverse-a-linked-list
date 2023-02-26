# linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def push(self,ele):
        newnode = Node(ele)
        newnode.next = self.head
        self.head = newnode
    def pop(self):
        temp = self.head
        self.head = self.head.next
        print("element poped is",temp.data)
    def print(self):
        temp = self.head
        while(temp.next!=None):
            print(temp.data,end="->")
            temp = temp.next
        print(temp.data)
    def atlast(self,ele):
        newnode = Node(ele)
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = newnode
        newnode.next = None
    def atposition(self,n,ele):
        newnode = Node(ele)
        if self.head is None:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            for i in range(1,n-1):
                if temp!=None:
                    temp = temp.next
            newnode.next=temp.next
            temp.next=newnode
ob = Linkedlist()
ob.push(10)
ob.push(20)
ob.push(30)
ob.push(40)
ob.print()
ob.atlast(100)
ob.print()
ob.atposition(3,100)
ob.print()
