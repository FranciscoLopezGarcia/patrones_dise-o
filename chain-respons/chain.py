class Handler:
    def handle(self, request):
        pass

    def set_next(self, handler):
        self.next_handler = handler

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request.type == "tipo1":
            print("Handler 1 has handled the request")
            return True
        else:
            return False

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request.type == "tipo2":
            print("Handler 2 has handled the request")
            return True
        else:
            return False

class ConcreteHandler3(Handler):
    def handle(self, request):
        if request.type == "tipo3":
            print("Handler 3 has handled the request")
            return True
        else:
            return False

class ConcreteHandler4(Handler):
    def handle(self, request):
        if request.type == "tipo4":
            print("Handler 4 has handled the request")
            return True
        else:
            return False

class Request:
    def __init__(self, type):
        self.type = type

def client_code(chain):
    requests = ["tipo1", "tipo2", "tipo3", "tipo4"]
    for request in requests:
        print(f"Sending request of type {request}...")
        chain.handle(Request(request))

def main():
    chain = ConcreteHandler1()
    chain.set_next(ConcreteHandler2())
    chain.set_next(ConcreteHandler3())
    chain.set_next(ConcreteHandler4())

    client_code(chain)

if __name__ == "__main__":
    main()
