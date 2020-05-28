# 536. Construct Binary Tree from String


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def print(self, indent=""):
        print(indent + str(self.val))
        indent += "  "
        if self.left:
            self.left.print(indent)
        if self.right:
            self.right.print(indent)


class StringToTree:
    def parse(self, s):
        self.i = 0
        return self._parse(s)

    def _parse(self, s):
        if self.i >= len(s):
            return None
        val = 0
        while self.i < len(s) and s[self.i].isdigit():
            val = val * 10 + int(s[self.i])
            self.i += 1
        node = Node(val)

        if self.i < len(s) and s[self.i] == '(':
            self.i += 1
            node.left = self._parse(s)
        if self.i < len(s) and s[self.i] == ')':
            self.i += 1
            return node
        if self.i < len(s) and s[self.i] == '(':
            self.i += 1
            node.right = self._parse(s)
        if self.i < len(s) and s[self.i] == ')':
            self.i += 1
        return node


if __name__ == "__main__":
    s2t = StringToTree()
    node = s2t.parse("4(2(3)(1))(6(5))")
    node.print()
