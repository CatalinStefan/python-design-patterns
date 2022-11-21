import time
from threading import Thread, Lock


class Singleton(type):
    _instances = {}
    _lock = Lock()

    def __call__(self, *args, **kwargs):
        with self._lock:
            if self not in self._instances:
                instance = super().__call__(*args, **kwargs)
                time.sleep(1)
                self._instances[self] = instance
        return self._instances[self]


class NetworkDriver(metaclass=Singleton):
    def log(self):
        print(f"{self}\n")


def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton


if __name__ == '__main__':
    # Single thread
    # s1 = create_singleton()
    # s2 = create_singleton()

    # Multi thread
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)
    p1.start()
    p2.start()
