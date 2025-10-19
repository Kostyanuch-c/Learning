from typing import Optional


class DoublyLinkedListNode:
    def __init__(
            self,
            value: int,
            prev: Optional['DoublyLinkedListNode'] = None,
            next: Optional['DoublyLinkedListNode'] = None
    ):
        self.prev = prev
        self.value = value
        self.next = next

    # def __str__(self) -> str:
    #     return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None

    # def __str__(self) -> str:

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current))
            current = current.next
        return f'{self.head.prev} -> {" -> ".join(nodes)} -> {self.tail.next}' if nodes else "Empty list"

    def insert_begin(self, value: int) -> None:
        if self.head is None:
            node = DoublyLinkedListNode(value=value)
            self.head = node
            self.tail = node
        else:
            node = DoublyLinkedListNode(value=value, prev=None, next=self.head)
            self.head.prev = node
            self.head = node

    def insert_end(self, value: int) -> None:
        if self.tail is None:
            node = DoublyLinkedListNode(value=value)
            self.head = node
            self.tail = node
        else:
            node = DoublyLinkedListNode(value=value, prev=self.tail, next=None)
            self.tail.next = node
            self.tail = node

    def remove_begin(self) -> int | None:
        if self.head is None:
            return None

        result = self.head.value

        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return result

    # def fore(self):
    #     current = self.head
    #     while current is not None:
    #         yield current.value
    #         current = current.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next


def main():
    x = DoublyLinkedList()
    print(repr(x))
    x.insert_begin(2)
    print(x)
    x.insert_begin(3)
    print(x)

    x.insert_end(52)
    x.insert_end(51)
    print(x)

    x.insert_begin(11)
    print(x)

    x.remove_begin()
    print(x)

    y = DoublyLinkedList()
    y.insert_begin(2)
    print(y)

    y.remove_begin()
    print(y)




if __name__ == "__main__":
    main()
