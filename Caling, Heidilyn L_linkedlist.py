class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        """Print friendly step chain ending with X"""
        current = self.head
        if current is None:
            print("X (No more steps!)")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("X")

    def to_pylist(self):
        """Return Python list of node data (useful for debugging)"""
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

    # begginning
    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    # b) remove_at_end(self)
    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed = self.head.data
            self.head = None
            return removed
        current = self.head
        while current.next.next:
            current = current.next
        removed = current.next.data
        current.next = None
        return removed

    # c) remove_at(self, data)
    def remove_at(self, data: str):
        if self.head is None:
            return None
        # If head matches
        if self.head.data == data:
            removed = self.head.data
            self.head = self.head.next
            return removed
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None: 
            return None
        removed = current.next.data
        current.next = current.next.next
        return removed

    # add at end
    def add(self, data: str):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node


def setup_sample_steps():
    L = LinkedList()
    L.add("A. Prepare")
    L.add("B. Cook rice")
    L.add("C. Place on mat")
    L.add("D. Roll")
    L.add("E. Eat")
    return L


def normalize_step_input(inp: str):
    """User may input 'A' or 'a' or 'A.' or 'A. Prepare' -> normalize to full step if possible."""
    inp = inp.strip()
    if not inp:
        return ""
    # Accept single-letter like A or a
    letter = inp.upper()
    if len(letter) == 1 and letter in "ABCDE":
        mapping = {
            "A": "A. Prepare",
            "B": "B. Cook rice",
            "C": "C. Place on mat",
            "D": "D. Roll",
            "E": "E. Eat",
        }
        return mapping[letter]
    # If user entered the full name already, return it as-is (trimmed)
    return inp


if __name__ == "__main__":
    steps = setup_sample_steps()

    print("🍣 HOW TO MAKE SUSHI - STEP LIST 🍣")
    steps.display()

    commands = {
        "add",
        "remove_beginning",
        "remove_end",     
        "remove_at",
        "view",
        "quit",
    }

    while True:
        cmd = input("\nEnter action (add, remove_beginning, remove_end, remove_at, view, quit): ").strip()
        if not cmd:
            print("Invalid action. Try:", ", ".join(sorted(commands)))
            continue

        cmd_low = cmd.lower()

        if cmd_low == "quit":
            print("Exiting. Bye!")
            break

        elif cmd_low == "view":
            print("\nCurrent Steps (friendly):")
            steps.display()
            print("List items (debug):", steps.to_pylist())

        elif cmd_low == "add":
            item = input("Enter step text to add (e.g. 'F. New step' or 'G. Some step'): ").rstrip("\n")
            if item:
                steps.add(item)
                print("Added. Current steps:")
                steps.display()
            else:
                print("Nothing added (empty input).")

        elif cmd_low == "remove_beginning":
            removed = steps.remove_beginning()
            if removed is None:
                print("List is empty. Nothing removed.")
            else:
                print("Removed from beginning:", removed)
            steps.display()

        elif cmd_low in ("remove_end", "remove_at_end"):
            removed = steps.remove_at_end()
            if removed is None:
                print("List is empty. Nothing removed.")
            else:
                print("Removed at end:", removed)
            steps.display()

        elif cmd_low == "remove_at":
            raw = input("Enter which step to remove (letter A-E or full step): ")
            step_name = normalize_step_input(raw)
            if not step_name:
                print("No input provided.")
                continue
            removed = steps.remove_at(step_name)
            if removed is None:
                print(f"Step not found or already removed: '{step_name}'")
                print("Debug list items:", steps.to_pylist())
            else:
                print("Removed:", removed)
            steps.display()

        else:
            print("Invalid action. Try:", ", ".join(sorted(commands)))
