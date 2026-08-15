from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional[Node] = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    
    # Insert at the end
    def insert(self, data: int) -> None:
        new_node = Node(data)

        # Empty list
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        # Find the last node
        current: Node = self.head

        while current.next != self.head:
            # Pylance knows current.next could be None,
            # so we check it before assigning.
            if current.next is None:
                raise RuntimeError("Broken circular list")

            current = current.next

        # current is now the last node
        current.next = new_node
        new_node.next = self.head

    
    # Insert at a specific index
    def insert_at(self, index: int, data: int) -> bool:
        if index < 0:
            return False

        new_node = Node(data)

        # Empty list
        if self.head is None:
            if index != 0:
                return False

            self.head = new_node
            new_node.next = new_node
            return True

        # Insert at head
        if index == 0:
            last: Node = self.head

            while last.next != self.head:
                if last.next is None:
                    raise RuntimeError("Broken circular list")

                last = last.next

            new_node.next = self.head
            last.next = new_node
            self.head = new_node

            return True

        # Find node currently at index
        previous: Node = self.head
        current: Optional[Node] = self.head.next

        position = 1

        while current is not None and current != self.head:

            if position == index:
                new_node.next = current
                previous.next = new_node
                return True

            previous = current
            current = current.next
            position += 1

        # Insert at the end
        if position == index and current == self.head:
            new_node.next = self.head
            previous.next = new_node
            return True

        return False

    
    # Display / traversal
    def display(self) -> None:
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

    
    # Delete the head
    def delete_head(self) -> None:
        if self.head is None:
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            return

        # Find last node
        last: Node = self.head

        while last.next != self.head:
            if last.next is None:
                raise RuntimeError("Broken circular list")

            last = last.next

        # Move head
        self.head = self.head.next

        # Last node points to new head
        last.next = self.head

    
    # Delete a specific value
    def delete(self, data: int) -> bool:
        if self.head is None:
            return False

        # Deleting head
        if self.head.data == data:
            self.delete_head()
            return True

        previous: Node = self.head
        current: Optional[Node] = self.head.next

        while current is not None and current != self.head:

            if current.data == data:
                previous.next = current.next
                return True

            previous = current
            current = current.next

        return False



# Example
cll = CircularLinkedList()

cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.display()
cll.insert_at(1, 15)
cll.display()
cll.delete(15)
cll.display()
cll.delete_head()
cll.display()
