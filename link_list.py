class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        if current is None:
            print("X")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("X")

    # a. Remove at the beginning
    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    # b. Remove at the end
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

    # c. Remove by data
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


linked_list = LinkedList()
linked_list.insert_at_end("Assemble")
linked_list.insert_at_end("Prepare")
linked_list.insert_at_end("Roll")
linked_list.display()

print("Removed at beginning:", linked_list.remove_beginning())
linked_list.display()

print("Removed at end:", linked_list.remove_at_end())
linked_list.display()

print("Removed specific (Prepare):", linked_list.remove_at("Prepare"))
linked_list.display()
