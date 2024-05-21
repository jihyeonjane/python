class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age 
        # private 멤버 변수 : 클래스 안에서 자유롭게 접근 및 사용 가능
        self.job = job


    def _hello(self):
        print(f"Hello, I'm {self.name}, I'm {self.__age}")

    def update_age(self, age):
        if age < 0:
            raise ValueError("양수 입력 요망")
        else :
            self.__age = age
            print(f"Now I'm {self.__age}!")

if __name__=="__main__":
    man = Person("John", 12)
    man._hello()
    man.update_age(13)