from reciver import Receiver

class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.do_something()

def client_code(command):
    command.execute()

if __name__ == "__main__":
    command = ConcreteCommand(Receiver())
    client_code(command)
