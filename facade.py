from dataclasses import dataclass


class ComplexSystemStore:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cache = {}
        print(f"Reading data from file: {filepath}")

    def store(self, key: str, value: str):
        self.cache[key] = value

    def read(self, key: str):
        return self.cache[key]

    def commit(self):
        print(f"Storing cached data to file {self.filepath}")


@dataclass
class User:
    login: str


# Facade
class UserRepository:
    def __init__(self):
        self.system_preferences = ComplexSystemStore("/data/default.prefs")

    def save(self, user: User):
        self.system_preferences.store("USER_KEY", user.login)
        self.system_preferences.commit()

    def find_first(self):
        return User(self.system_preferences.read("USER_KEY"))


if __name__ == '__main__':
    user_repo = UserRepository()
    user = User("john")

    user_repo.save(user)

    retrieved_user = user_repo.find_first()
    print(retrieved_user.login)
