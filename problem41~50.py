# 문제 41: 소수 판별
from math import sqrt, ceil
n = int(input('소수인지 확인하고자 하는 숫자를 입력하세요.!'))
checkNum = 0
for i in range(2, ceil(sqrt(n))):
    if n % i == 0:
        checkNum = 1

if checkNum:
    print('소수가 아닙니다.')
else:
    print('소수입니다.')


# 문제 42:2020년
# 2020년은 1월 1일은 수요일(WEN)입니다.
# 두 수 a, b를 입력받아 2020년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성해라
# 요일의 이름은 일요일부터 토요일까지 각각 SUN, MON, TUE, WED, THU, FRI, SAT 입니다.

weekdays = {1:'WED', 2:'THU', 3:'FRI', 4:'SAT', 5:'SUN', 6:'MON', 0:'TUE'}
months   = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
totalDay = 0
import sys
f    = sys.stdin
a, b = map(int, f.readline().split(" "))

for i in range(a):
    totalDay = months.get(i, 0) + totalDay
totalDay = totalDay + b

print(weekdays[totalDay % 7])

# 문제 43: 10진수를 2진수로
# 우리가 흔히 사용하는 숫자 1, 8, 19, 28893 등등..은 10진수 체계입니다.
#  이를 컴퓨터가 알아 들을 수 있는 2진수로 바꾸려고 합니다. 어떻게 해야할까요?
# 예를들어 13은 2^3 + 2^2 + 2^0 = 13 이기 때문에 1101으로 표현합니다.
def two_number(n):
    two_list = []
    while(True):
        if n >= 2:
            two_list.append(str(n % 2))
            n = n // 2
        else: break
    two_list.append(str(n))
    two_list.reverse()
    return ''.join(two_list)
number = int(input("2진수로 변경할 숫자를 입력하세요."))
print(two_number(number))

# 문제 44: 각 자리수의 합
# 사용자가 입력한 양의 정수의 각 자리수의 합을 구하는 프로그램을 만들어 주세요.
number = input('입력하실 숫자를 입력하세요!')
print(sum(list(map(int, list(number)))))

# 문제 45: time 함수 사용하기
from time import time
curr_time = time()
# 1년 = 365 * 24 * 60 * 60
print(int(1970 + curr_time // (365 * 24 * 60 * 60))) # 현재 날짜는 2020

# 문제 46 : str 자료형의 응용
# 1부터 20까지의 모든 숫자를 일렬로 놓고 모든 자리수의 총합을 구히시오.
final_list = []
for i in range(1, 21, 1):
    final_list.extend(list(map(int, list(str(i)))))
print(sum(final_list))

# 문제 47 : set 자료형의 응용
# 바울랩에서는 3월 29일 제주대학교에서 '제주 빅데이터 사회혁신 해커톤' 행사를 주최하게 되었습니다.
# 이에 구글 설문지를 배포하였으나 제주대학생들이 중복해서 n개씩 설문지를 제출하였습니다.
# 중복된 데이터들을 삭제하여 실제 접수 명단이 몇 명인지 알고 싶습니다.

people = [
    ('이호준', '01050442903'),
    ('이호상', '01051442904'),
    ('이준호', '01050342904'),
    ('이호준', '01050442903'),
    ('이준',  '01050412904'),
    ('이호',  '01050443904'),
    ('이호준', '01050442903'),
]
print(len(set(people)))

# 문제 48 : 대소문자 바꿔서 출력하기
# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작석하세요,
str_list = list(input('문자열을 입력하세요.'))
final_list = []
for i in str_list:
    if i == i.upper():
        final_list.append(i.lower())
    else:
        final_list.append(i.upper())

print(''.join(final_list))

# 문제 49 : 최댓값 구하기
# 순서가 없는 10개의 숫자가 공백으로 구분되어 주어진다. 주어진 숫자들 중 최댓값을 반환하라.
number_list = list(map(int, input('10개의 숫자를 공백으로 구분하여 입력하세요.').split(" ")))
print(max(number_list))

# 문제50 : 버블정렬 구현하기
# 버블정렬은 두 인접한 원소를 검사하여 정렬하는 방법을 말합니다. 시간 복잡도는 느리지만 코드가 단순하기 때문에
# 자주 사용됨.
data = [1, 2, 3, 4, 5, 6, 7]
def bubble(data):
    print(data)
    for i in range(len(data)-1, 1, -1):
        toggle = True
        for j in range(i):
            if data[j] > data[j+1]:
                toggle = False
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
        if(toggle): break
    print(data)





