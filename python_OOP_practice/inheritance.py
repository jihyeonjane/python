# 다중상속. 다이아몬드 상속 관련

class A:
    def method(self):
        print("I'm A")

class B(A):
    def method(self):
        print("I'm B")

class C(A):
    def method(self):
        print("I'm C")

class D(B, C):
    pass

d = D()
# 뭐가 실행될까....
d.method()
# B가 실행됐음.....!

# 아래의 mro를 통해 호출 순서 확인할 수 있음.
print(D.mro())