# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self, top):
        self.top = top

    def print_structure(self):
        current_node = self.top

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):

        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top:
            self.top = self.top.next


first_node = Node("1")
my_stack = Stack(first_node)

second_node = Node("2")
my_stack.push(second_node)

third_node = Node("3")
my_stack.push(third_node)

my_stack.print_structure()

my_stack.pop()

my_stack.print_structure()