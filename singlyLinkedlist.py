class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insertfirst(self,data):
        new_node = node(data)
        if (self.head==None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertlast(self,data):
        new_node = node(data)
        new_node.next = None
        if(self.head == None):
            self.head = new_node
        cnode = self.head
        while (cnode.next != None):
            cnode = cnode.next
        cnode.next = new_node

    def delfirst(self):
        cnode = self.head
        self.head = cnode.next 
        cnode.next = None
        del cnode

    def dellast(self):
        lnode = self.head
        while (lnode.next != None):
            lnode = lnode.next
        lnode = None
        del lnode

    def printlist(self):
        lnode = self.head
        while lnode:
            print(lnode.data)
            lnode = lnode.next
            

listobj =linkedlist()

listobj.insertfirst(20)
listobj.insertfirst(30)
listobj.insertfirst(40)
listobj.insertfirst(50)
listobj.insertlast(60)
listobj.insertlast(70)


listobj.printlist()











