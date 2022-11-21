from __future__ import annotations


class ChatUser:
    mediator = None

    def __init__(self, name: str):
        self.name = name

    def set_mediator(self, med: Mediator):
        self.mediator = med

    def send(self, msg: str):
        print(f"{self.name}: Sending message {msg}")
        self.mediator.send_message(msg, self)

    def receive(self, msg: str):
        print(f"{self.name}: Receiving message {msg}")


class Mediator:
    users = []

    def add_user(self, user: ChatUser):
        self.users.append(user)
        user.set_mediator(self)

    def send_message(self, msg: str, user: ChatUser):
        for u in self.users:
            if u != user:
                u.receive(msg)


if __name__ == '__main__':
    mediator = Mediator()
    alice = ChatUser("Alice")
    bob = ChatUser("Bob")
    carol = ChatUser("Carol")

    mediator.add_user(alice)
    mediator.add_user(bob)
    mediator.add_user(carol)

    carol.send("Hi everyone!")
