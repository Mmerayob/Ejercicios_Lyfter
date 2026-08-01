# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# # No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.


class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

        if self.head and self.tail and self.head != self.tail:
            self.head.next = self.tail
        elif self.head and not self.tail:
            self.tail = self.head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push_left(self, new_node):

        new_node.next = self.head
        self.head = new_node


    def push_right(self, new_node):

        self.tail.next = new_node
        self.tail = new_node
    
    def pop_left(self):
        if self.head:
            self.head = self.head.next

    
    def pop_right(self):

        current_node = self.head

        while current_node.next != self.tail:
            current_node = current_node.next

        current_node.next = None
        self.tail = current_node


first_node = Node("1")
second_node = Node("2")
my_double_ended_queue = DoubleEndedQueue(first_node,second_node)

third_node = Node("3")
my_double_ended_queue.push_right(third_node)

fourth_node = Node("4")
my_double_ended_queue.push_right(fourth_node)

my_double_ended_queue.print_structure()

my_double_ended_queue.pop_left()

my_double_ended_queue.print_structure()

my_double_ended_queue.pop_right()

my_double_ended_queue.print_structure()