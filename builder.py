class NetworkService:
    def __init__(self):
        self.components = {}

    def add(self, key: str, value: str):
        self.components[key] = value

    def show(self):
        print(self.components)


class NetworkServiceBuilder:
    def __init__(self):
        self._service = NetworkService()

    def add_target_url(self, url: str):
        self._service.add("URL", url)

    def add_auth(self, auth: str):
        self._service.add("Authorization", auth)

    def add_caching(self, cache: int):
        self._service.add("Cache-Control", cache)

    def build(self) -> NetworkService:
        service = self._service
        self._service = NetworkService()
        return service


if __name__ == '__main__':
    builder = NetworkServiceBuilder()
    builder.add_target_url("google.com")
    
    service1 = builder.build()
    service1.show()

    builder.add_target_url("youtube.com")
    builder.add_auth("abc123")
    builder.add_caching(60000)

    service2 = builder.build()
    service2.show()




