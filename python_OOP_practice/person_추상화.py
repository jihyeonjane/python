from abc import ABC

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job

    # 추상클래스
    @abstractmethod
    def introduce(self):
        pass

    def hello(self):
        print(f"Hello, I'm {self.name}")

    def update_age(self, age):
        if age < 0:
            raise ValueError("양수 입력 요망")
        else :
            self.age = age
            print(f"Now I'm {self.age}!")

# if __name__=="__main__":
#     man = Person("John", 12)
#     man.hello()
#     man.update_age(13)