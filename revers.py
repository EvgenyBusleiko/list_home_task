from random import randint as r
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class List_1:
    def __init__(self,data):
        new_node = Node (data)
        self.start_node=new_node
    def print_l(self):
        if self.start_node is None:
            print("список пустой")
            return
        n=self.start_node
        while n is not None:
            print(n.data, end=' ')
            n=n.next
        print()
    def insert_start(self,data):
        new_node=Node(data)
        new_node.next=self.start_node
        self.start_node=new_node
    def insert_end(self,data):
        new_node=Node(data)
        n=self.start_node
        while n.next:
            n=n.next
        n.next=new_node
    def delete_start(self):
        if self.start_node is None:
            print("список пустой")
            return
        self.start_node=self.start_node.next
    def delete_end(self):
        n=self.start_node
        while n.next.next is not None:
            n=n.next
        n.next=None
    def saerch (self,x):
        n = self.start_node
        while n is not None:
            if n.data==x:
                return True
            n=n.next
        return False
    def reverse (self):

        n = self.start_node
        l = List_1(n.data)
        while n.next is not None:

            n = n.next
            l.insert_start(n.data)

        l.print_l()
    def buble (self):

        flag=True
        while flag:
            n = self.start_node
            flag=False

            while n.next is not None:

                if n.data>n.next.data:
                    n.data,n.next.data=n.next.data,n.data
                    flag=True
                n=n.next

l2=List_1(1)
for i in range(199):
    l2.insert_start(r(0,10))
l2.print_l()
l2.buble()
l2.print_l()
l2.reverse()
l2.print_l()