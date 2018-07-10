class Target(object):
    def specific_request(self):
        return 'Hello Adapter Pattern !'


class Adapter(object):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()


if __name__ == "__main__":
    client = Adapter(Target())
    print(client.request())


