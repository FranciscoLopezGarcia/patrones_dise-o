class Product:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        pass

class ConcreteProduct1(Product):
    def __init__(self):
        super().__init__("Producto 1")

    def do_something(self):
        print("Estoy haciendo algo como producto 1")
