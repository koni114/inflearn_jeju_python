## 제주코딩베이스캠프 ##
## 11~20번 문제 풀기 ##

# 문제11 : for를 이용한 기본 활용
s = 0
number = 100
for i in range(number):
    s += i
print(s)

#  문제12 :게임 캐릭터 클래스 만들기

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print("파이어볼")

x = Wizard(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()

# 문제 13 : 몇 번째 행성인가요?
# 태양계 : 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성, 명왕성
listA = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성','명왕성']
number = int(input("행성의 숫자를 입력하세요"))
print(listA[number-1])

# 문제 14 : 3의 배수인가요 ?
# 만약 수가 3의 배수라면 '짝' 이라는 글자를, 3의 배수가 아니라면 n을 그대로 출력
number = int(input("랜덤 숫자 하나를 말하세요"))
if(number % 3  == 0):
    print("짝")
else:
    print(number)


# 문제 15 : 자기소개
name = input("자기이름을 말하세요!")
print("안녕하세요 저는 ", name, "입니다", sep = "")

# 문제 16 : 로꾸꺼
# 문장이 입력되면 거꾸로 출력하는 프로그램
sentence = input("문장을 입력하세요")
print(sentence[::-1])

# 문제 17 : 놀이기구 키 제한
height = int(input('키를 입력하세요'))
if(height > 150):
    print("YES")
else:
    print("NO")

# 문제 18 : 평균 점수
#  국어, 수학, 영어 시험을 보았는데, 평균 점수 구하기
a, b, c = map(int, input("국어, 영어, 수학 점수를 입력하세요").split(" "))
print((a + b + c) // 3)

# 문제 19 : 제곱을 구하자
# 공백으로 구분하여 두 숫자 a,b가 주어지면 a의 b승을 구하는 프로그램 작성
a,b = map(int, input("두 수를 입력하세요").split(" "))
print(a ** b)

# 문제 20 : 몫과 나머지
# 공백으로 구분하여 두 숫자가 주어짐.
# 첫 번째 숫자로 두 번째 숫자를 나누었을 때 그 몫과 나머지를 공백으로 구분하여 출력
a, b = map(int, input("두 수를 입력하세요").split(" "))
print(a // b, end = " ")
print(a % b)


