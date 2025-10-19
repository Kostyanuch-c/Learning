class AvlTreeNode:
    def __init__(self, value, parent=None):
        self.left = None  # ссылка на левый дочерний узел
        self.right = None  # ссылка на правый дочерний узел
        self.balance_factor = 0  # показатель сбалансированности
        self.parent = parent  # ссылка на родителя
        self.value = value  # полезная нагрузка

    def __repr__(self):
        return f"TreeNode({self.value}, left={repr(self.left)}, right={repr(self.right)})"
