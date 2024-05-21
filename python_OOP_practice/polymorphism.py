from programmer import Programmer
from actor import Actor

# 다형성(Polymorphism) 예시
# people이라는 리스트에 넣어서 여러개 한번에 실행해보기
people = [
    Programmer("Jane",30,"Python"),
    Actor("Kim", 20, "Parasite")
]

for person in people:
    person.introduce()
    person.hello()
    person.update_age(person.age+1) # 한살씩 먹도록 설정..굳굳