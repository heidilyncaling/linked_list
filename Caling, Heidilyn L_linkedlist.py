class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        if current is None:
            print("X")  # When the list is empty
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("X")  # End of list symbol changed from None to X

    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data

    def remove_at(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None:
            return None
        removed_data = current.next.data
        current.next = current.next.next
        return removed_data

if __name__ == "__main__":
    X = LinkedList()

    X.head = Node("ASSEMBLE")
    second = Node("PREPARE")
    third = Node("ROLL")
    X.head.next = second
    second.next = third

    print("Initial linked list:")
    X.display()

    print("\nRemoving beginning:")
    R = X.remove_beginning()
    print("R =", R)
    X.display()

    print("\nRemoving at end:")
    removed_end = X.remove_at_end()
    print("Removed at end =", removed_end)
    X.display()

    print("\nRemoving PREPARE (remaining node):")
    removed_data = X.remove_at("PREPARE")
    print("Removed =", removed_data)
    X.display()