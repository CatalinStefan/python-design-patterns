from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        print(f"Real image: loading {filename}")

    def display(self):
        print(f"Real image: displaying {self.filename}", end="\n\n")


class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        print(f"Proxy image: displaying {self.filename}")
        if not self.real_image:
            print("From disk")
            self.real_image = RealImage(self.filename)
        else:
            print("From cache")
        self.real_image.display()


if __name__ == '__main__':
    image = ProxyImage("test.jpg")
    # load image from disk
    image.display()
    # load image from cache
    image.display()
