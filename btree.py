class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def search(self, k, x=None):
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)

    def insert(self, k):
        r = self.root
        if len(r.keys) == (2 * self.t) - 1:
            s = BTreeNode()
            self.root = s
            s.child.insert(0, r)
            self.split_child(s, 0)
            self.insert_non_full(s, k)
        else:
            self.insert_non_full(r, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]
        if not y.leaf:
            z.child = y.child[t:(2 * t)]
            y.child = y.child[0:(t - 1)]

    def remove(self, k):
        stack = []

        n = self.root
        i = 0
        while n is not None:
            i = 0
            while i < len(n.keys) and k > n.keys[i]:
                i += 1
            if i < len(n.keys) and k == n.keys[i]:
                break
            stack.append((n, i))
            n = n.child[i]

        if n is not None:
            if n.leaf:
                del n.keys[i]
            else:
                y = n.child[i]
                while not y.leaf:
                    stack.append((y, len(y.keys) - 1))
                    y = y.child[-1]

                n.keys[i] = y.keys[-1]
                i = len(y.keys) - 1

                if len(y.keys) >= self.t:
                    n = y
                else:
                    while len(n.keys) < self.t:
                        if len(stack) == 0:
                            break
                        parent, index = stack.pop()
                        sibling_index = index + 1 if index < len(parent.keys) else index - 1

                        sibling = parent.child[sibling_index]

                        if len(sibling.keys) >= self.t:
                            if index < len(parent.keys):
                                y.keys.append(parent.keys[index])
                                parent.keys[index] = sibling.keys.pop(0)
                                if not y.leaf:
                                    y.child.append(sibling.child.pop(0))
                            else:
                                if index < len(parent.keys):
                                    parent.keys.append(parent.keys.pop(index))
                                    y.keys.append(sibling.keys.pop(0))
                                    if not y.leaf:
                                        y.child.append(sibling.child.pop(0))
                                else:
                                    y.keys.insert(0, parent.keys.pop(index - 1))
                                    parent.keys.insert(index - 1, sibling.keys.pop())

                            if not y.leaf:
                                y.child.append(sibling.child.pop(0))
                        else:
                            if index < len(parent.keys):
                                y.keys.append(parent.keys.pop(index))
                                y.keys += sibling.keys
                                if not y.leaf:
                                    y.child += sibling.child
                            else:
                                parent.keys.append(parent.keys.pop(index - 1))
                                parent.keys += sibling.keys
                                if not parent.leaf:
                                    y.child += sibling.child

                        parent.child.pop(sibling_index)

                    if len(n.keys) >= self.t:
                        n = y

        # Verifique se a raiz está vazia e atualize a raiz, se necessário
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.child[0]

    def traverse(self, x, level=0):
        if isinstance(x, BTreeNode):
            s = ''
            seen = set()
            for i in range(len(x.keys)):
                if not x.leaf:
                    s += self.traverse(x.child[i], level + 1)
                if x.keys[i] not in seen:
                    s += f"{' ' * (level * 4)}{x.keys[i]}\n"
                    seen.add(x.keys[i])
            if not x.leaf:
                s += self.traverse(x.child[len(x.keys)], level + 1)
            return s
        else:
            return ''

tree = BTree(2)
tree.insert(10)
tree.insert(20)
tree.insert(5)
tree.insert(6)
tree.insert(12)
tree.insert(30)
tree.insert(7)
tree.insert(17)
tree.remove(20)
print(tree.traverse(tree.root))
