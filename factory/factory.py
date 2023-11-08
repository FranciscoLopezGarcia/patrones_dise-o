from products import Factory

def client_code(factory):
    product = factory.create_product("producto1")
    product.do_something()

if __name__ == "__main__":
    factory = Factory()
    client_code(factory)
