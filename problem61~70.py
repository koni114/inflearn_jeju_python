# 문제 61: 문자열 압축하기
# 문자열을 입력받고 연속되는 문자열을 압축해서 표현하고 싶습니다.
from collections import Counter

str_text = 'aaabbbcdddd'
Counter(str_text)

## 내장 함수 미사용으로 해결해보기
# 초기값 저장(init_v), num = 1 init variables
# 1 index부터 시작. init_v에 값이 같으면 num

import sys
from collections import deque
f = sys.stdin
str_text = str.strip(f.readline())
result_v = deque()

i = 0
num = 1
init_v = str_text[0]
while(i < len(str_text)-1):
    # 만약 i+1 의 값과 같으면, num +=1
    # 만약 i+1 같지 않으면, result_v.append
    if init_v == str_text[i+1]:
        i += 1
        num += 1
    else:
        result_v.append(str(init_v))
        result_v.append(str(num))
        init_v = str_text[i+1]
        num = 1
        i += 1

result_v.append(str(init_v))
result_v.append(str(num))

print(''.join(result_v))

# 문제62: 20190923 출력하기
# 20190923을 출력합니다. 아래 기준만 만족하면 됩니다.

# 1. 코드내에 숫자가 없어야 합니다.
# 2. 파일 이름이나 경로를 사용해서는 안됩니다.
# 3. 시간 날짜 함수를 사용해서는 안됩니다.
# 4. 에러 번호 출력을 이용해서는 안됩니다.
# 5. input을 이용해서는 안됩니다.
string = 'aabcccccccccddd'
a = string.count('a')
b = string.count('b')
c = string.count('c')
d = string.count('d')
e = string.count('e')
print(str(a) + str(e) + str(b) + str(c) + str(e) + str(c) + str(a) + str(d))

# 문제63 : 친해지고 싶어
# 한국대학교 김한국교수님은 학생들과 친해지기 위해서 딸에게 줄임말을 배우기로 했습니다.
# 딸은 '복잡한 세상 편하게 살자' 라는 문장을 '복세편살'로 줄여 말합니다.
# 어떤 입력이 주어지면 앞 글자만 줄여 출력하도록 해주세요

import sys
from collections import deque
f = sys.stdin
text_list = list(f.readline().split(" "))
result_text = deque()
for text in text_list:
    result_text.append(text[0])
print(''.join(result_text))

# 문제 64: 이상한 엘레베이터
# 정량 N에 정확히 맞춰야만 움직이는 화물용 엘레베이터가 있습니다.
# 화물은 7kg, 3kg 두 가지이며 팔이 아픈 은후는 가장 적게 화물을 옮기고 싶습니다.

# 예를 들어 정량이 24kg이라면 3kg 8개를 옮기는 것 보다는
# 7kg 3개, 3kg 1개 즉 4개로 더 적게 옮길 수 있습니다.

# 입력 : 정량 N이 입력됨
# 출력 : 가장 적게 옮길 수 있는 횟수를 출력
#       만약 어떻게 해도 정량 N이 되지 않는다면 -1를 출력

import sys
f = sys.stdin
N = int(str.strip(f.readline()))

if N < 7:
    dp = [N for _ in range(8)]
else:
    dp = [N for _ in range(N+1)]

dp[3] = 1
dp[6] = 2
dp[7] = 1

for i in range(N+1):
    if i-3 >= 0:
        tmp_min = dp[i-3] + 1
    if i-7 >= 0:
        tmp_min = min(tmp_min, dp[i-7] + 1)
    if i >= 7:
        if tmp_min == N:
            dp[i] = N
        else:
            dp[i] = min(dp[i], tmp_min)

if(dp[N] == N):
    print('-1')
else:
    print(dp[N])

# 64번 이상한 엘리베이터 -> 답안
# 3kg, 7kg이기 때문에 가능 -> 2개이기 때문에,,
# 3을 빼 나가면서, 7로 나눠 떨어지는 순간이 있으면, 몫을 결과 값에 더해줌.

N = int(input())
result = 0

while True:
    if N % 7 == 0:
        result += N // 7
        print(result)
        break
    else:
        N -= 3
        result += 1
    if N < 0:
        print(-1)
        break

# 문제65 : 변형된 리스트
# a,b list를 번갈아가면서 출력시키시요~
a = [1,2,3,4]
b = ['a', 'b', 'c', 'd']
result_list = []

for i, value in enumerate(zip(a, b)):
    if i % 2 == 0:
        result_list.append(list(value))
    else:
        result_list.append(list(value[::-1]))

print(result_list)

# 문제66 : 블럭탑쌓기
# 탑을 쌓기 위해 각 크기별로 준비된 블럭들을 정해진 순서에 맞게 쌓아야 함
# 순서에 맞게 쌓지 않으면 무너질 수 있음
# 예를 들면 정해진 순서가 BAC라면 A 다음 C가 쌓아져야 합니다.
# 선행으로 쌓아야 하는 블럭이 만족된 경우라면 탑이 무너지지 않습니다.

# B를 쌓지 않아도 A와 C를 쌓을 수 있습니다.
# B 다음 블럭이 C가 될 수 있습니다.



## 문제 70: 행렬 곱하기
## 행렬 2개가 주어졌을 때 곱할 수 있는 행렬인지 확인하고 곱할 수 있다면 그 결과를, 곱할 수 없다면 -1를 출력하는
## 프로그램을 만들어 주세요.
def solution(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return -1
    return [[sum(a*b for a,b in zip(i, j)) for i in zip(*matrix_b)] for j in matrix_a ]
a = [[1, 2], [2, 4]]
b = [[1, 0], [0, 3]]
print(solution(a, b))