class Node:
    def __init__(self, data):
        self.data = data
        self.prev: Node | None = None
        self.next: Node | None = None


class DoublyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    
    # APPEND
    def append(self, data):
        new_node = Node(data)

        # Empty list
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        # Non-empty list
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    
    # PREPEND
    def prepend(self, data):
        new_node = Node(data)

        # Empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Non-empty list
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    
    # FIND
    def find(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

        return None

    
    # GET
    def get(self, index):
        # Invalid index
        if index < 0 or index >= self.size:
            return None

        # Search from HEAD
        if index < self.size // 2:

            current = self.head

            # Because index is valid and we're starting
            # from head, current should exist.
            if current is None:
                return None

            for _ in range(index):
                if current.next is None:
                    return None

                current = current.next

            return current

        # Search from TAIL
        else:

            current = self.tail

            if current is None:
                return None

            steps = self.size - 1 - index

            for _ in range(steps):
                if current.prev is None:
                    return None

                current = current.prev

            return current

    
    # SET
    def set(self, index, data):
        node = self.get(index)

        if node is None:
            return False

        node.data = data
        return True

    
    # INSERT BEFORE
    def insert_before(self, current, data):
        new_node = Node(data)

        # Empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Current is the head
        elif current == self.head:

            new_node.next = current
            current.prev = new_node
            self.head = new_node

        # Current is somewhere after head
        else:

            previous = current.prev

            # Safety check for type checker
            if previous is None:
                return False

            new_node.prev = previous
            new_node.next = current

            previous.next = new_node
            current.prev = new_node

        self.size += 1
        return True

    
    # INSERT AFTER
    def insert_after(self, current, data):
        new_node = Node(data)

        # Empty list
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        # Current is the tail
        elif current == self.tail:

            current.next = new_node
            new_node.prev = current
            self.tail = new_node

        # Current is somewhere before tail
        else:

            next_node = current.next

            # Safety check
            if next_node is None:
                return False

            new_node.prev = current
            new_node.next = next_node

            current.next = new_node
            next_node.prev = new_node

        self.size += 1
        return True

    
    # INSERT AT
    def insert_at(self, index, data):
        # Valid insertion indexes:
        # 0 <= index <= size
        if index < 0 or index > self.size:
            return False

        # Beginning
        if index == 0:
            self.prepend(data)
            return True

        # End
        if index == self.size:
            self.append(data)
            return True

        # Middle
        target = self.get(index)

        if target is None:
            return False

        return self.insert_before(target, data)

    
    # DELETE NODE
    def delete(self, node):
        if node is None:
            return False

        # Only node in list
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None

        # Deleting HEAD
        elif node == self.head:

            next_node = node.next

            if next_node is None:
                return False

            self.head = next_node
            next_node.prev = None

        # Deleting TAIL
        elif node == self.tail:

            previous = node.prev

            if previous is None:
                return False

            self.tail = previous
            previous.next = None

        # Deleting middle node
        else:

            previous = node.prev
            next_node = node.next

            if previous is None or next_node is None:
                return False

            previous.next = next_node
            next_node.prev = previous

        # Detach the deleted node
        node.prev = None
        node.next = None

        self.size -= 1

        return True

    
    # DELETE AT
    def delete_at(self, index):
        if index < 0 or index >= self.size:
            return False

        node = self.get(index)

        if node is None:
            return False

        return self.delete(node)

    
    # POP
    def pop(self):
        if self.tail is None:
            return None

        node = self.tail

        # Only node
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # More than one node
        else:

            previous = node.prev

            if previous is None:
                return None

            self.tail = previous
            previous.next = None

        # Detach returned node
        node.prev = None
        node.next = None

        self.size -= 1

        return node

    
    # LENGTH
    def length(self):
        return self.size

    
    # TRAVERSE FORWARD
    def traverse_forward(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    
    # TRAVERSE BACKWARD
    def traverse_backward(self):
        current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev

    
    # REVERSE
    def reverse(self):
        current = self.head

        while current is not None:
            current.prev, current.next = (
                current.next,
                current.prev
            )

            # After swapping:
            # current.prev points to the node
            # we need to process next.
            current = current.prev

        self.head, self.tail = self.tail, self.head


if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.prepend(5)

    dll.traverse_forward()
    print("size:", dll.size)

    dll.traverse_backward()

    print("get(2):", dll.get(2))

    dll.set(2, 25)

    dll.traverse_forward()

    dll.insert_at(2, 15)

    dll.traverse_forward()

    dll.delete_at(2)

    dll.traverse_forward()

    node = dll.pop()

    print("popped:", node)

    dll.traverse_forward()

    dll.reverse()

    dll.traverse_forward()