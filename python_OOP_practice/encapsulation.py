from programmer import Programmer

dave = Programmer("Dave", 42, "Python")

# update_age에는 age 음수에 대한 에러 설정했으나, 그냥 age는 설정 못했음
# 이럴 때 접근 제어자가 필요함.
dave.__age = -1

# 캡슐화를 통해 age에 음수가 들어가도 정상적인 값인 42가 출력됨
dave._hello()
