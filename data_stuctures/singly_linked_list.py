class LinkedListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.value} -> {self.next}"

    def __repr__(self):
        return str(self)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        self.head = LinkedListNode(value, self.head)

    def __str__(self):
        if self.head:
            return f"{self.head.value} -> {self.head.next}"
        return "Empty"

    def __repr__(self):
        return str(self)

    def insert(self, index: int, new_value: int) -> None | bool:
        if index == 0:
            self.add(new_value)
        if self.head is None:
            self.head = LinkedListNode(new_value, None)
        current = self.head
        while current.next is not None and index > 1:
            current = current.next
            index -= 1
        current.next = LinkedListNode(value=new_value, next=current.next)

    def remove(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next

        return value

    def delete(self, index: int):
        if index == 0 or self.head.next is None:
            self.remove()
        elif self.head is None:
            return None
        else:
            current = self.head
            while current.next.next is not None and index > 1:
                current = current.next
                index -= 1

            value = current.next.value
            current.next = current.next.next

            return value

    def reverse(self):
        if self.head is None:
            return
        current = self.head
        new = LinkedList()
        while current.next is not None:
            new.add(current.value)
            current = current.next
        new.add(current.value)
        return new


def main():
    x = LinkedList()
    x.add(1)

    x.add(3)
    x.add(4)
    x.add(5)
    x.add(6)
    print(x)




if __name__ == '__main__':
    main()
