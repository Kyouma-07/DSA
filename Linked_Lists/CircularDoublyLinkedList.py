from typing import Optional

class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

   
    # Insert at the end

    def insert(self, data: int) -> None:
        new_node = Node(data)

        # Empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

            return

        # Pylance knows head is Node here,
        # but tail is still Optional[Node].
        if self.tail is None:
            raise RuntimeError("Broken list: head exists but tail is None")

        # Connect new node
        new_node.prev = self.tail
        new_node.next = self.head

        # Connect existing nodes
        self.tail.next = new_node
        self.head.prev = new_node

        # Update tail
        self.tail = new_node

   
    # Insert at a specific index
   
    def insert_at(self, index: int, data: int) -> bool:
        if index < 0:
            return False

        new_node = Node(data)

       
        # Case 1: Empty list
       
        if self.head is None:
            if index != 0:
                return False

            self.head = new_node
            self.tail = new_node

            new_node.next = new_node
            new_node.prev = new_node

            return True

        # Tail must exist if head exists
        if self.tail is None:
            raise RuntimeError("Broken list: head exists but tail is None")

       
        # Case 2: Insert at head
       
        if index == 0:
            new_node.next = self.head
            new_node.prev = self.tail

            self.head.prev = new_node
            self.tail.next = new_node

            self.head = new_node

            return True

        # Find node currently at index
       
        current: Node = self.head
        position = 0

        while position < index and current != self.tail:
            if current.next is None:
                raise RuntimeError("Broken circular list")

            current = current.next
            position += 1

       
        # Case 3: Insert at the end
        if position == index and current == self.tail:
            new_node.prev = self.tail
            new_node.next = self.head

            self.tail.next = new_node
            self.head.prev = new_node

            self.tail = new_node

            return True

       
        # Invalid index
        if position != index:
            return False

       
        # Case 4: Insert before current
        if current.prev is None:
            raise RuntimeError("Broken list: current.prev is None")

        new_node.prev = current.prev
        new_node.next = current

        current.prev.next = new_node
        current.prev = new_node

        return True

   
    # Display forward
    def display_forward(self) -> None:
        if self.head is None:
            print("List is empty")
            return

        current: Node = self.head

        while True:
            print(current.data, end=" ")

            if current.next is None:
                raise RuntimeError("Broken circular list")

            current = current.next

            if current == self.head:
                break

        print()

   
    # Display backward
    def display_backward(self) -> None:
        if self.tail is None:
            print("List is empty")
            return

        current: Node = self.tail

        while True:
            print(current.data, end=" ")

            if current.prev is None:
                raise RuntimeError("Broken circular list")

            current = current.prev

            if current == self.tail:
                break

        print()

   
    # Delete a specific node by reference
    def delete_node(self, node: Optional[Node]) -> bool:
        if node is None:
            return False

        # Empty list
        if self.head is None or self.tail is None:
            return False

       
        # Case 1: Only one node
        if self.head == self.tail:
            if node != self.head:
                return False

            self.head = None
            self.tail = None

            node.next = None
            node.prev = None

            return True

       
        # Case 2: Delete head
        if node == self.head:
            if self.head.next is None:
                raise RuntimeError("Broken list")

            self.head = self.head.next

            self.head.prev = self.tail
            self.tail.next = self.head

            node.next = None
            node.prev = None

            return True

       
        # Case 3: Delete tail
        if node == self.tail:
            if self.tail.prev is None:
                raise RuntimeError("Broken list")

            self.tail = self.tail.prev

            self.tail.next = self.head
            self.head.prev = self.tail

            node.next = None
            node.prev = None

            return True

       
        # Case 4: Delete middle node
        if node.prev is None or node.next is None:
            raise RuntimeError("Broken list")

        node.prev.next = node.next
        node.next.prev = node.prev

        # Fully detach node
        node.prev = None
        node.next = None

        return True

   
    # Delete first node containing a value
    def delete(self, data: int) -> bool:
        if self.head is None:
            return False

        current: Node = self.head

        while True:
            if current.data == data:
                return self.delete_node(current)

            if current.next is None:
                raise RuntimeError("Broken circular list")

            current = current.next

            if current == self.head:
                break

        return False


if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    cdll.insert(10)
    cdll.insert(20)
    cdll.insert(30)
    cdll.insert(40)

    cdll.display_forward()
    cdll.display_backward()
    cdll.insert_at(2, 25)
    cdll.display_forward()
    cdll.delete(25)
    cdll.display_forward()
    cdll.delete(10)
    cdll.display_forward()
    cdll.delete(40)
    cdll.display_backward()
