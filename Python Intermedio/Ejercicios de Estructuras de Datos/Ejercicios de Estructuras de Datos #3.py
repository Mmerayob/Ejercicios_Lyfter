# Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root: Node


    def __init__(self,root):
        self.root = root

    def print_structure(self):

        def print_nodes(node):
            if node is None:
                return
            else:
                print(node.data)
                print_nodes(node.left)
                print_nodes(node.right)

        print_nodes(self.root)

left_node = Node("Hijo Izquierdo")
right_node = Node("Hijo Derecho")
root = Node("Raiz",left=left_node,right=right_node)

tree = BinaryTree(root)
tree.print_structure()

