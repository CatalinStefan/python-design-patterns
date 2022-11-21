class NetworkService:
    def __init__(self, url: str = "", auth: str = "", cache: int = 0):
        self.components = {}
        if url:
            self.components["URL"] = url
        if auth:
            self.components["Authorization"] = auth
        if cache:
            self.components["Cache-Control"] = cache

    def show(self):
        print(self.components)


if __name__ == '__main__':
    service1 = NetworkService(url="google.com")
    service1.show()

    service2 = NetworkService(url="youtube.com", auth="abc123", cache=60000)
    service2.show()