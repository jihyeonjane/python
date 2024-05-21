from person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job="Programmer")
        self.language = language

    def introduce(self):
        super()._hello()
        print(f"저는 {self.language}로 프로그래밍이 가능합니다.")