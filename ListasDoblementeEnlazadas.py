class Node:
    def __init__(self, value):
        self.value = value
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None

class ListasDoblementeEnlazadas:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, value):
    new_node = Node(value)
    #si está vacía
    if(self.size == 0):
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.derecha = new_node
      new_node.izquierda = self.tail
      self.tail = new_node

    self.size += 1
