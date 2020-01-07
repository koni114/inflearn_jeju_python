# 문제 51: mergeSort를 만들어보자
def mergeSort(arrList):
    arr_len = len(arrList)
    if arr_len <= 1: return arrList
    mid = arr_len // 2
    arr_1 = mergeSort(arrList[:mid])
    arr_2 = mergeSort(arrList[mid:])
    result = []

    while len(arr_1) >= 1 and len(arr_2) >= 1:
        if arr_1[0] < arr_2[0]:
            result.append(arr_1.pop(0))
        else:
            result.append(arr_2.pop(0))

    while len(arr_1) >= 1:
        result.append(arr_1.pop(0))

    while len(arr_2) >= 1:
        result.append(arr_2.pop(0))

    return result

ex_list = [180, 145, 165, 45, 170, 175, 173, 171]
mergeSort(ex_list)

# 문제 52: quick sort
# quickSort 알고리즘을 구현해보세요!

arrList = [1,2,3,4,1]
def quickSort(arrList):
    arr_len = len(arrList)
    if arr_len <= 1:
        return arrList

    value = arrList.pop(len(arrList) // 2)
    group_1, group_2 = [], []

    for i in range(len(arrList)):
        if arrList[i] < value:
            group_1.append(arrList[i])
        else:
            group_2.append(arrList[i])

    return quickSort(group_1) + [value] + quickSort(group_2)

quickSort([1,2,3,4,1])

# 문제 53 : 괄호 문자열
# 괄호 문자열이란, 괄호 기호인, {}, [], ()를 말한다.
# 그 중 괄호의 모양이 바르게 구성 된 문자열을 바른 문자열, 그렇지 않은 문자열을 바르지 않은 문자열이라 부르도록 하자.
# 입력으로 주어진 괄호 문자열이 바른 문자열인지 바르지 않은 문자열인지 YES와 NO로 구분된 문자열을 출력하시오.
import sys
from collections import deque
f = sys.stdin
test_arr = list(str.strip(f.readline()))
result_arr = deque()

def solution(test_arr):
    for i in range(len(test_arr)):
        if test_arr[i] == '(':
            result_arr.append(1)
        else:
            if len(result_arr) < 1:
                return "NO"
            result_arr.popleft()

    if len(result_arr) == 0:
        return "YES"
    else:
        return "NO"

solution(test_arr)

# 문제 54 : 연속되는 수
# 은주는 놀이공원 아르바이트를 하고 있습니다.
# 은주가 일하는 놀이공원에서는 현재 놀이공원 곳곳에 숨겨진 숫자 스탬프를 모아 오면 선물을 주는 이벤트를 하고 있습니다.
# 숫자 스탬프는 매일 그 수와 스탬프에 적힌 숫자가 바뀌지만 그 숫자는 항상 연속됩니다.
# 그런데 요즘 다른 날에 찍은 스탬프를 가지고 와 선물을 달라고 하는 손님이 있습니다.

# 스탬프에 적힌 숫자가 공백으로 구분되어 주어지면 이 숫자가 연속수인지 아닌지
# "YES" 와 "NO" 로 판별하는 프로그램을 작성하세요.
import sys
f = sys.stdin
test_arr = list(map(int, f.readline().split(" ")))
def solution(test_arr):
    test_arr = sorted(test_arr)
    for i in range(len(test_arr) - 1):
        if test_arr[i] + 1 != test_arr[i+1]:
            return 'NO'

    return 'YES'

print(solution(test_arr))

# 문제 55 : 하노이의 탑
# 하노이의 탑은 프랑스 수학자 에두아르드가 처음으로 발표한 게임.
# 다음의 코드문에서 나머지 부분을 채워 넣으세요!
movingPath = []
def hanoi(number, start, target, sub):
    if number == 1:
        movingPath.append([start, target])
        return None

    hanoi(number-1, start, sub, target)
    movingPath.append([start, target])
    hanoi(number-1, sub, start, target)

hanoi(3, 'A', 'B', 'C')
print(movingPath)
print(len(movingPath))

# 문제 56 : 리스트의 함수 응용
# 다음의 딕셔너리가 주어졌을 때 한국의 면적과 가장 비슷한 국가의 그 차이를 출력하세요.
nationWidth = {
    'korea': 220877,
    'Russia': 17098242,
    'China' : 9596951,
    'France' : 543965,
    'Japan'  : 377915,
    'England' : 242900
}

min_value = 10000000000
min_nation = ''

for nation, width in nationWidth.items():
    if width < min_value and  nation != 'korea':
        min_value = width
        min_nation = nation

print(min_nation, abs(nationWidth['korea'] - min_value))

# 문제 57: 내장함수 응용하기
# 1 ~ 1000까지 1의 개수는 몇개일까요 ?
def countN(n):
    countN = str(list(range(n+1))).count('1')
    return countN

# 문제 58 : 콤마찍기
# 123456789 -> 123,456,789 입력하기
import sys
f = sys.stdin
str_text = list(str.strip(f.readline()))
str_len = len(str_text)
if str_len % 3 == 0:
    start_v = list(range(3, str_len, 3))
else:
    start_v = list(range(str_len % 3, str_len, 3))

for i in range(len(start_v)):
    str_text.insert(i+start_v[i], ',')

print(''.join(str_text))

# 문제 59: 빈칸채우기
# 총 문자열의 길이는 50으로 제한
# 사용자가 문자열을 입력하면 그 문자열 가운데 정렬을 해주고, 나머지 빈 부분에는 "=" 입력

# 주의 사항
# 50이 넘는 경우에는 문자열을 잘라서 그대로 출력
# 50이 넘지 않는경우에는
#  50 - 해당 길이 // 2 계산
# 만약 % 2 == 1인경우 오른쪽이나 왼쪽에 = 를 하나 더 붙여줌

import sys
f = sys.stdin
text = str.strip(f.readline())
text_len = len(text)

if text_len >= 50:
    print(text[:50])
else:
    n = (50 - text_len) // 2
    c = (50 - text_len) % 2

    if c == 1:
        print("="*(1+n) + text + "="*n)
    else:
        print("=" * (n) + text + "=" * n)

# 문제 60: enumerate
# 새학기가 되어 이름을 가나다 순으로 배정하고 번호를 매기려고 합니다
# 코드에 입력된 이름을 다음과 같이 출력해주세요

student = ['강은지', '김유진', '박현서', '최성흔', '홍유진', '박지호',
           '권윤일', '김채리', '한지호', '김진이', '김민호', '강채연']

for i, name in enumerate(student):
    print('번호: '+ str(i+1) + ', 이름: ' + name)

