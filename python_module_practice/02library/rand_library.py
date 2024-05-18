import random

# 난수 생성
randnum = random.randint(1,30)
print(randnum)

# 여러 랜덤 숫자 생성
for i in range(5):
    print(random.randint(1,30))


# 설정한 시퀀스에서 랜덤 초이스
basket = ['apple','lemon','peach','watermelon']
print(random.choice(basket))