# Membuat kelas Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, nextNode):
        self.next = nextNode
    
    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

# Membuat kelas LinkedList
class LinkedList:
    def __init__(self):
        self.first = None

# Membuat method add
    def add(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
        else:
            sem = self.first
            while sem.getNext():
                sem = sem.getNext()
            sem.setNext(new_node)

# Membuat method insert
    def insert(self, value, index):
        if index == 0:
            self.add(value)
            return
        
        position = 0
        current_node = self.first
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.getNext()

        if current_node is not None:
            new_node = Node(value)
            new_node.setNext(current_node.getNext())
            current_node.setNext(new_node)
        else:
            print("Index tidak ada")

# Membuat method remove
    def remove(self, index):
        if self.first is None:
            print("List kosong")
            return
        
        if index == 0:
            self.first = self.first.getNext()
            return
        
        current_node = self.first
        prev_node = None
        current_index = 0

        while current_node is not None and current_index < index:
            prev_node = current_node
            current_node = current_node.getNext()
            current_index += 1
        
        if current_node is None:
            print("Index out of range")
            return
        
        if prev_node is not None:
            prev_node.setNext(current_node.getNext())

# Membuat method swap
    def swap(self, index1, index2):
        if index1 == index2:
            return
        
        prev1 = None
        node1 = self.first
        for i in range(index1):
            if node1 is None:
                print('Index 1 tidak ada')
                return
            prev1 = node1
            node1 = node1.getNext()

        prev2 = None
        node2 = self.first
        for i in range(index2):
            if node2 is None:
                print('Index 2 tidak ada')
                return
            prev2 = node2
            node2 = node2.getNext()

        if node1 is None or node2 is None:
            print('Salah satu atau kedua index tidak ada')
            return

        if prev1:
            prev1.setNext(node2)
        else:
            self.first = node2

        if prev2:
            prev2.setNext(node1)
        else:
            self.first = node1

        node1_next = node1.getNext()
        node2_next = node2.getNext()

        node1.setNext(node2_next)
        node2.setNext(node1_next)

# Membuat method get
    def get (self):
        current_node = self.first
        while current_node is not None:
            print(current_node.getValue())
            current_node = current_node.getNext()

# Membuat objek list dari kelas LinkedList
testList = LinkedList()

# Menambahkan value menggunakan method add 
testList.add('k')
testList.add('e')
testList.add('l')
testList.add('o')
testList.add('m')
testList.add('p')
testList.add('o')
testList.add('k')
testList.add(7)

# Mencetak hasil list setelah memakai method add
print('\nSemua yang ada di list: \n')
testList.get()

# Menukar value menggunakan method swap berdasarrkan index yang ingin ditukar
testList.swap(8,0)

# Mencetak hasil list setelah memakai method swap
print('\nList setelah di swap: \n')
testList.get()


# Menghapus value menggunakan method remove berdasarrkan index
testList.remove(1)

# Mencetak hasil list setelah memakai method remove
print('\nList setelah di remove: \n')
testList.get()

