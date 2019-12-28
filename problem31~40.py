# 문제35: Factory 함수 사용하기
def one(n):
    def two(value):
        sq =  value ** n
        return sq
    return two

a = one(2)
b = one(3)
c = one(4)

print(a(10))
print(b(10))
print(c(10))

# 문제 36: 구구단 출력하기
n = int(input("구구단을 출력할 숫자를 입력하세요"))
for i in range(1, 10):
    print(i*n, end = " ")
print("")

# 문제 37: count 사용하기
from collections import Counter
name_str = list(input("학생들이 뽑은 후보군을 입력하세요").split(" "))
c        = Counter(name_str)

final_name  = ''
final_value = 0

for name, value in c.items():
    if final_value < value:
        final_value = value
        final_name  = name
print(final_name, '(이)가 총 ', final_value, '표로 반장이 되었습니다.',  sep = "")

# 문제 38: 호준이의 아르바이트

score_list = sorted(list(map(int, input("채점할 시험 점수를 입력하세요").split(" "))), reverse = True)
candy_score = 0
score = 0

for i in range(len(score_list)):
    if score == 3: break
    candy_score = i+1
    if not len(score_list)-1 == i:
        if score_list[i] > score_list[i+1]:
            score = score + 1

print(candy_score)



# 문제 39: 오타 수정하기
str_1 = input('혜원이가 잘못 입력한 문자열')
print(str_1.replace('q', 'e'))

# 문제 40: 놀이동산에 가자

import sys
from collections import deque
f = sys.stdin
weight = int(f.readline())
n      = int(f.readline())
human_weight = deque()
check_weight = 0
final_score = 0

for i in range(n):
    human_weight.append(int(f.readline()))

for i in range(len(human_weight)):
    check_weight = check_weight + human_weight[i]
    if check_weight > weight: break
    final_score = i+1

print(final_score)