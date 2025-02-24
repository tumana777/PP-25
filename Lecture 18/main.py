# from collections import deque
#
# q = deque(maxlen=15)
#
# q.append(1)
# q.append(5)
# q.append(2)
# q.append(6)
# q.append(3)
#
# q.appendleft(2)
# q.appendleft(4)

# popped = q.pop()
# left_popped = q.popleft()

# print(left_popped)

# print(popped)

# print(q.count(4))

# q.remove(2)

# print(q.index(2))

# q.insert(1, "Hello")
#
# print(q)

# from queue import Queue
#
# q = Queue(maxsize=4)

# print(q.qsize())

# q.put(4)
# q.put(1)
# q.put(7)
# q.put(3)
# q.put(9)

# q.put_nowait(5)
# q.put_nowait(6)
# q.put_nowait(7)
# q.put_nowait(8)

# print(q.full())

# q.put_nowait(9)

# print(q.empty())

# q.get()
# q.get()
# q.get()
# q.get()
# q.get()

# print(q.empty())

# q.get_nowait()
# q.get_nowait()
# q.get_nowait()
# q.get_nowait()
# q.get_nowait()

# print(q.queue)
# print(q.qsize())

import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are: ")
        self._print_parents(self.root, None)

    def generate_graph(self):
        graph = nx.DiGraph()
        self._add_edges(self.root, graph)
        return graph

    def _add_edges(self, node, graph):
        if node:
            if node.left:
                graph.add_edge(node.key, node.left.key)
                self._add_edges(node.left, graph)
            if node.right:
                graph.add_edge(node.key, node.right.key)
                self._add_edges(node.right, graph)

    def plot_tree(self):
        graph = self.generate_graph()

        pos = self._get_tree_layout(graph)
        plt.figure(figsize=(16, 8))
        nx.draw(graph, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=12, font_weight="bold",
                arrows=True)
        plt.title("Binary Search Tree")
        plt.show()

    def _get_tree_layout(self, graph):
        pos = self._hierarchical_layout(graph)
        return pos

    def _hierarchical_layout(self, graph):
        pos = {}
        self._set_node_positions(self.root, 0, 0, pos)
        return pos

    def _set_node_positions(self, node, x, y, pos):
        if node is not None:
            pos[node.key] = (x, y)
            if node.left:
                self._set_node_positions(node.left, x - 1, y - 1, pos)
            if node.right:
                self._set_node_positions(node.right, x + 1, y - 1, pos)

bst = BST()


bst.insert(5)
bst.insert(3)
bst.insert(9)
bst.insert(6)
bst.insert(12)
# bst.insert(8)
bst.insert(10)
bst.insert(11)

# bst.insert(4)

bst.plot_tree()

bst.print_parents()
















