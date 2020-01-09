# 1. list 함수를 사용할 때, 정수 값 1개를 list 함수를 사용하면 error 발생!

# 2. char를 이용하는 방법에 대해서 잘 알고 있는가?

# 2.1 int -> chr function
# 기본적으로 숫자는 char 형태로 형변환이 가능
# 알파벳이 시작되는 숫자는 기억해두자
# A : 65
# a : 97

chr(65)
chr(97)

# 2.2 chr -> int
# chr 형태에서 int 로 변환 : ord function

ord('a')
ord('A')

# List comprehension practice
# 기본적으로 파이썬을 한다는 의미는 list comprehension을 자유자재로 다룰 줄 알아야 함

# 크게 list 껍대기를 벗길것이냐, 벗기지 않을 것이냐에 따라서 크게 나뉨

# 괄호를 벗기고 싶으면, 기존의 n중 포문을 한줄로 나열했다고 생각하고 코딩
# 괄호를 벗기고 싶지 않다면, 괄호 안에있는 값들이 바로 n중 for문으로 적용된다고 생각하자!!

## 1. row 내의 element 접근하기
# 1.1 두개 괄호가 쳐 있을 때, 괄호를 벗기고 요소만 꺼내고 싶을 때,
a = [[1,2,3], [4,5,6], [7,8,9]]
matrix_low = [elements for row in a for elements in row]
print(matrix_low)

# 1.2 세개 괄호가 쳐 있을 때, 괄호를 벗기고 요소만 꺼내고 싶을 때,
b = [[[1,2,3], [4,5,6], [7,8,9]], [['a','b','c'], ['d', 'e', 'f']]]
[elements for row in b for row_matrix in row for elements in row_matrix]

## 2. 리스트를 살리면서 element 접근하기
# 2.1 다중 리스트 만들기(리스트 안의 리스트 만들기)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix_square = [[elements ** 2 for elements in matrix_b] for matrix_b in matrix ]
print(matrix_square)

############################################
## dfs, bfs 사용시 , numpy 사용 여부 생각해보자 #
## why? 내가 원하는 2차원 배열을 slicing을 통해  #
## 해낼 수 있기 때문 !
############################################
import numpy as np
test = [[1,2,3,4], [3,4,5,5], [4,5,6,7]]
test = np.array(test)
test[1:2, 2:3]    # 기존의 array만 가지고는 사용 불가능하다

# Tip
# 함수에서 입력되는 list는 주소를 참조함을 항상 조심하자.
# -> global 명령어를 주지 않더라도, 원본 list도 같이 바뀐다. -> 조심하자

# 예시)
arr = []
def solution(arr, s):
    arr.append('check')
    return arr

solution(arr, 'a')
print(arr)

