# 정렬 알고리즘 정리

## 핵심 키워드
* Bubble Sort  
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort

### 1. 버블 정렬(Bubble Sort)
#### 정렬 방법 설명
* 매번 연속(i, i+1)된 두개 인덱스를 비교하여, 오름차순 또는 내림차순 Rule에 따라 값을 정렬하는 방법
* 오름차순인 경우, 1 cycle를 돌 때 마다 가장 큰 값이 가장 끝 위치에 오게됨
* 내림차순인 경우, 1 cycle를 돌 때 마다 가장 작은 값이 가장 끝 위치에 오게됨
* 각 싸이클 마다 가장 큰 값이 제일 마지막 위치에 저장되기 때문에 <b/>(cycle 당 전체 배열의 크기 - 현재까지 순환한 바퀴 수)</b> 만큼만 반복해 주면 됨

#### 성능을 개선하는 방법
*  꼭 모든 cycle(배열의 길이 만큼)을 다 돌아야 정렬되는 것은 아니다. 중간에 다 정렬 될 수도 있다. 이를 확인하여 이미 정렬이 다 이루어 졌다면, 정렬을 종료한다!  
방법은 각각 싸이클마다 한 번이라도 swap이 이루어 지는지 check하면 된다

* 각 싸이클마다 모든 인덱스를 확인할 필요가 없다. 위에서 설명했다시피 한 싸이클이 진행될때마다 배열의 마지막에는 가장 크거나(오름차순), 가장 작은(내림차순)이 위치하게 된다.  
따라서 싸이클이 진행될때마다 비교하고자 하는 인덱스의 총 길이를 1개씩 줄인다!

#### python 코드
~~~
arr1 = [5,4,3,2,1]
arr2 = [182, 180, 1, 30, 999, 33, 10]
arr3 = [1]
arr4 = [3,3,3,4,4,1,1,5]

1. bubble sort
def bubbleSort(arrList):
    for i in range(len(arrList)- 1):
        for j in range(len(arrList) - (i+1)):
            if arrList[j] > arrList[j+1]:
                arrList[j], arrList[j+1] = arrList[j+1], arrList[j]

    return arrList

bubbleSort(arr1)
bubbleSort(arr2)
bubbleSort(arr3)
bubbleSort(arr4)
~~~

### 2. 삽입 정렬(Insert Sort)
#### 정렬 방법 설명
* 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘
* 매 순서마다 해당 원소를 삽입할 수 있는 위치를 찾아 해당 위치에 넣음
* 두 번째 인덱스부터 시작하여 해당 인덱스 앞의 자료들과 비교하여 삽입할 위치를 지정한 후 해당 값을 삽입
* 처음 key 값은 두 번째 자료부터 시작

#### python 코드
~~~
def insertSort(arrList):
    for i in range(1, len(arrList)):
        for j in range(i):
            if arrList[j] >= arrList[i]:
                arrList.insert(j, arrList.pop(i))

    return arrList

insertSort(arr1)
insertSort(arr2)
insertSort(arr3)
insertSort(arr4)
~~~
### 3. 병합 정렬(merge Sort)
#### 정렬 방법 설명
* 분할 정복(divide and conquer) 방법을 이용해서 정렬을 수행함.
* 더이상 쪼갤 수 없을 때까지 정렬을 쪼개고, 병합하는 과정에서 정렬을 수행함
* <b/>분할(Divide)</b> : 입력 배열을 같은 크기의 2개 배열로 나눔
* <b/>정복(Conquer)</b> : 부분 배열을 정렬. 부분 배열의 크기가 충분히 작지 않으면 recursive call을 이용하여 분할 정복 방법을 적용
* <b/>결합(Conbine)</b> : 정렬된 부분 배열들을 하나의 배열에 합병
* 시간복잡도
  * 분할 단계 : 비교 연산과 이동 연산이 수행되지 않는다
  * 합병 단계 : 전체 사이클은 쪼개진 배열을 두개씩 합치는 과정이 있으므로, log2n. 각 싸이클 마다 길이 n 만큼 비교를 하므로, n. 따라서 nlog2n 만큼 시간이 걸림
* T(n) = nlog₂n(비교) + 2nlog₂n(이동) = 3nlog₂n = O(nlog₂n)  
비교를 한 후 이동을 각각 한번씩 해야 하므로, n, 2n만큼의 시간이 걸림
#### python 코드
~~~
def mergeSort(arrList):
    arr_len = len(arrList)
    if arr_len <= 1: return arrList
    mid   = arr_len // 2
    arr_1 = mergeSort(arrList[:mid])
    arr_2 = mergeSort(arrList[mid:])

    arr_result = []

    while len(arr_1) >= 1 and len(arr_2) >= 1:
        if arr_1[0] > arr_2[0]:
            arr_result.append(arr_2.pop(0))
        else:
            arr_result.append(arr_1.pop(0))

    while len(arr_1) >= 1:
        arr_result.append(arr_1.pop(0))

    while len(arr_2) >= 1:
        arr_result.append(arr_2.pop(0))

    return arr_result

~~~
### 4. 선택 정렬(selection Sort)
#### 정렬 방법 설명
* BubbleSort 만큼 쉬운 정렬 방법 중 하나로써, 첫번째 인덱스부터 차례로 정렬되지 않은 인덱스들을 비교해  가장 작거나(오름차순), 가장 큰(내림차순) 값을 찾아 해당 인덱스에 차례로 setting 하는 정렬 방법
* 1 싸이클을 수행하고 나면 첫 번째 인덱스에 가장 작거나 큰 값이 위치하게 됨
* 시간복잡도
  * 비교 횟수
    * 두 개의 for 루프의 실행 횟수
    * 외부 루프: (n-1)번
    * 내부 루프(최솟값 찾기): n-1, n-2, ..., 2, 1번

  * 교환 횟수
    * 외부 루프의 실행 횟수와 동일
    * 한 번 교환하기 위하여 3번의 이동(SWAP 함수의 작업)이 필요하므로 3(n-1)번
*  (n-1) + (n-2) + … + 2 + 1 = n(n-1)/2 = O(n^2)

~~~
def selectionSort(arrList):
    for i in range(len(arrList) -1):
        tmp     = arrList[i]
        tmp_idx = i
        for j in range(i+1, len(arrList)):
            if tmp > arrList[j]:
                tmp     = arrList[j]
                tmp_idx = j

        if not tmp_idx == i:
            arrList[tmp_idx] = arrList[i]
            arrList[i] = tmp

    return arrList
~~~
### 5. 퀵 정렬(quick Sort)
#### 정렬 방법 설명
* 퀵 정렬은 분할 정복 알고리즘을 기반으로 구현됨
  * 리스트 중에 pivot(기준) index 하나를 선택
  * 피벗 앞에는 피벗보다 작은 값, 뒤에는 큰 값이 오도록 변경하여 리스트를 둘로 분할
  * 분할된 두 개 리스트 각각에 재귀적으로 이 과정을 반복
* 자세히 설명하려면 좀 더 복잡하게 설명을 해야하므로, 다른 블로그 참조!^^

#### python 코드
~~~
4. quick sort
내가 짜본 코드
def quickSort(arrList):
    if len(arrList) <= 1: return arrList
    high_idx = 1
    low_idx  = len(arrList)-1

    while high_idx <= low_idx:
        while high_idx <= low_idx:
            if arrList[0] < arrList[high_idx]:
                break
            else: high_idx = high_idx + 1

        while high_idx <= low_idx:
            if arrList[0] > arrList[low_idx]:
                break
            else: low_idx = low_idx - 1

        if high_idx < low_idx:
            arrList[high_idx], arrList[low_idx] = arrList[low_idx], arrList[high_idx]
            low_idx  = low_idx - 1
            high_idx = high_idx + 1

    arrList[0], arrList[low_idx] = arrList[low_idx], arrList[0]

    arrList[:low_idx]     = quickSort(arrList[:low_idx])
    arrList[low_idx + 1:] = quickSort(arrList[low_idx+1:])

    return arrList

구글링한 코드
3개의 list로 나누어서 확인.

def quick_sort(list):
    if len(list) <= 1 : return list
    pivot = list[len(list) // 2]
    less_arr, equal_arr, big_arr = [], [], []
    for i in list:
        if i < pivot : less_arr.append(i)
        elif i > pivot : big_arr.append(i)
        else: equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr, quick_sort(big_arr)

성능을 개선 시킨 코드: 메모리 할당을 줄이기 위해 성능 개선.

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
~~~
