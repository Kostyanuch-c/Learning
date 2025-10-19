import random
from typing import Optional


class BinaryTreeNode:
    def __init__(self, value: int, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value

    def find_node(self, value: int) -> Optional["BinaryTreeNode"]:
        node = self

        while node:
            if self.value == value:
                return node
            if self.value > value:
                node = self.right
            if self.value < value:
                node = self.left
        return None

    def __str__(self, level=0, indent='\t'):
        ret = f"{indent * level}{self.value}\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        else:
            ret += f"{indent * (level + 1)}None\n"
        if self.right:
            ret += self.right.__str__(level + 1)
        else:
            ret += f"{indent * (level + 1)}None\n"
        return ret

    def __repr__(self):
        return f"TreeNode({self.value}, left={repr(self.left)}, right={repr(self.right)})"

    def insert_node(self, value: int) -> None:
        return self._insert_node(value, self)

    def _insert_node(self, value: int, parent_node: "BinaryTreeNode") -> None:
        if value < parent_node.value:
            if parent_node.left is None:
                parent_node.left = BinaryTreeNode(value, parent_node)
            else:
                self._insert_node(value, parent_node.left)
        elif value > parent_node.value:
            if parent_node.right is None:
                parent_node.right = BinaryTreeNode(value, parent_node)
            else:
                self._insert_node(value, parent_node.right)

    def remove_node(self, value):
        new_root = self._remove_node(value, self)
        self.value = new_root.value
        self.left = new_root.left
        self.right = new_root.right
        return self

    def _remove_node(self, value: int, node: "BinaryTreeNode") -> Optional["BinaryTreeNode"]:
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove_node(value, node.left)
            return node
        elif value > node.value:
            node.right = self._remove_node(value, node.right)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                original = node
                node = node.right
                while node.left:
                    node = node.left
                node.right = self._remove_node(node.value, original.right)
                node.left = original.left
                return node

    def traverse_recursive(self, node):
        if node is not None:
            print(f"node = {node.value}")
            self.traverse_recursive(node.left)
            self.traverse_recursive(node.right)

    def traverse_with_stack(self):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            print(f"node = {current_node.value}")
            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)

    def traverse_with_queue(self):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(f"node = {current_node.value}")
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)


def main():
    binary_tree = BinaryTreeNode(random.choice(range(20)))

    [binary_tree.insert_node(random.randint(1, 22)) for _ in range(20)]

    print(binary_tree)
    # binary_tree.insert_node(25)
    # binary_tree.insert_node(14)
    # binary_tree.insert_node(55)
    # binary_tree.insert_node(49)
    # binary_tree.insert_node(30)
    # binary_tree.insert_node(51)
    # binary_tree.insert_node(56)
    # print(binary_tree)
    # print(binary_tree.traverse_recursive(node=binary_tree))
    # print(binary_tree.traverse_with_stack())
    # print(binary_tree.traverse_with_queue())


if __name__ == "__main__":
    main()
