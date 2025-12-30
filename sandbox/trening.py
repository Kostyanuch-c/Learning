from collections import deque
from copy import copy
from itertools import count
from modulefinder import Module


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        lines, *_ = self._build_tree()
        return "\n".join(lines)

    def __repr__(self):
        return str(self)

    def _build_tree(self):
        """Возвращает список строк, ширину и центр текущего узла."""
        # Базовый случай: нет детей
        if not self.left and not self.right:
            line = str(self.val)
            width = len(line)
            middle = width // 2
            return [line], width, middle

        # Рекурсивно строим левое и правое поддеревья
        left_lines, left_width, left_middle = self.left._build_tree() if self.left else ([], 0, 0)
        right_lines, right_width, right_middle = self.right._build_tree() if self.right else ([], 0, 0)

        val_str = str(self.val)
        val_width = len(val_str)

        # Строим строку с корнем и соединениями
        first_line = ' ' * left_middle + (' ' if left_width > 0 else '') + val_str + ' ' * (right_width - right_middle)
        second_line = ''
        if self.left:
            second_line += ' ' * left_middle + '/' + ' ' * (left_width - left_middle - 1 + val_width)
        if self.right:
            second_line += ' ' * right_middle + '\\' + ' ' * (right_width - right_middle - 1)

        # Объединяем левое и правое поддеревья построчно
        left_lines += [' ' * left_width] * max(0, len(right_lines) - len(left_lines))
        right_lines += [' ' * right_width] * max(0, len(left_lines) - len(right_lines))

        merged_lines = [l + ' ' * val_width + r for l, r in zip(left_lines, right_lines)]

        # Возвращаем список строк, общую ширину и центр текущего узла
        lines = [first_line]
        if second_line.strip():
            lines.append(second_line)
        lines.extend(merged_lines)
        total_width = left_width + val_width + right_width
        middle = left_width + val_width // 2
        return lines, total_width, middle


class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return 0, 0

            prev_root_left, prev_left = dfs(node.left)
            prev_root_right, prev_right = dfs(node.right)

            return (
                node.val + prev_left + prev_right,
                max(prev_root_left, prev_left) + max(prev_root_right, prev_right)
            )

        return max(dfs(root))


if __name__ == '__main__':
    root1 = TreeNode(2)
    left_node = TreeNode(1)
    right_node = TreeNode(3)
    root1.right = right_node
    root1.left = left_node
    # root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)
    # root1.right.right = TreeNode(1)

    # root1.left = left_node
    # root1.left.right = TreeNode(2)
    # root1.left.left = TreeNode(6)
    # root1.left.right.left = TreeNode(7)
    # root1.left.right.right = TreeNode(4)
    # root1.right = TreeNode(-300)
    # root1.right.left = TreeNode(-10)
    sol = Solution()

    print(sol.rob(root1))
    #
    # s = Solution()
    #
    # print(root1)
    # print(s.deleteNode(root1, 2))
