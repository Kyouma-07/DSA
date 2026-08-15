class Node:

    def __init__(self, data):
        self.data = data
        self.next: Node | None = None


class LinkedList:

    def __init__(self):
       self.head: Node | None = None


    #defining a method for linkedList traversal:
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end = " -> ")
            current = current.next

        print("None")



    #Method for inserting_values: #at_beginning:
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


    #insert_at_end
    def insert_at_end(self, data):
        new_node = Node(data)

        #case1: Empty_List:
        if self.head is None:
            self.head = new_node
            return

        #case2 : Not Empty
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
    

    #finding a node by value:
    def find_node(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return current
            current = current.next
        return None


    #insert_after a given node
    def insert_after(self, current , data):
        
        #if current node doesnt exist:
        if current is None:
            return

        new_node = Node(data)

        #connect the new node to old_node:
        new_node.next = current.next

        #connect the current to new_node
        current.next = new_node


    #finding the mid :
    def find_mid(self):
        slow = self.head
        fast = self.head


        while  slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    #delete node by value:
    def delete_node(self, value):
        prev = None
        current = self.head

        #search for the node
        while current is not None and current.data != value:
            prev = current
            current = current.next

        #if target not found:
        if current is None:
            return 

        #deleting the first node:
        if prev is None:
            self.head = current.next
            return

        #deleting the node (given node or last node)
        prev.next = current.next

    def reversing_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


if __name__ == "__main__":
    obj = LinkedList()

    obj.insert_at_beginning(60)
    obj.insert_at_beginning(50)
    obj.insert_at_beginning(40)
    obj.insert_at_beginning(30)
    obj.insert_at_beginning(20)
    obj.insert_at_beginning(10)

    print("After inserting at beginning:    ")
    obj.display()

    obj.insert_at_end(70)
    obj.insert_at_end(80)
    obj.insert_at_end(90)
    obj.insert_at_end(100)

    print("After Inserting at end:  ")
    obj.display()

    print("Finding a node:  ")
    node = obj.find_node(90)
    if node is not None:
        print(node.data)

    print("Inserting After a node:  ")
    #find the node first
    node = obj.find_node(30)
    #insert after that node
    obj.insert_after(node,35)
    obj.display()

    print("Fidning the mid of the linked List:  ")
    mid = obj.find_mid()

    if mid is not None:
        print(mid.data)


    #deleting a node:
    obj.delete_node(10)
    print("After Deleting: 10")
    obj.display()

    print("reversing a  linked List:    ")
    obj.reversing_list()
    obj.display()