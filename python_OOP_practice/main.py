from programmer import Programmer
from actor import Actor

jane = Programmer("Jane",30,"Python")

jane.introduce()

# super 덕분에 person함수 import 안해도 아래의 함수 실행 잘됨
jane.hello()

jane.update_age(31)


# 추상클래스 예시(추상클래스인 introduce 반드시 구현해야함.)

kim = Actor("Kim", 20, "Parasite")
kim.introduce()
kim.hello()