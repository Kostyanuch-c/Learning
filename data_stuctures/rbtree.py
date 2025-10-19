class RBTreeNode:
    def __init__(self, value, parent=None):
        self.left = None  # ссылка на левый дочерний узел
        self.right = None  # ссылка на правый дочерний узел
        self.is_red = False  # цвет узла. Если не красный, то считаем что узел черный
        self.parent = parent  # ссылка на родителя
        self.value = value  # полезная нагрузка