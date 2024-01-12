# Fundamentals of Sorting

## Sort는 무엇인가
* 여러 객체가 존재할 때 이들이 공통적으로 가지는 특징이 존재한다.
* 이를 비교하기 위한 규칙을 정한다.
* 해당 규칙에 따라 객체의 순서를 재배열하는 것을 sorting, 정렬이라 한다.
* 비교하는 규칙은 전이법칙을 만족해야한다
  * a > b, b > c일 경우 a > c 이다.
* 두 가지 대상을 비교할 때 다음의 세 가지 관계 중 하나를 만족한다
  * a > b, a = b, a < b

## 어떨 때 해당 객체들의 모음은 sort되었다 할 수 있는가
* 비교 규칙에 맞지 않은 순서대로 정렬된 객체들의 짝을 inversion이라 정의하자.
  * ex) 수를 크기 순서대로 정렬할 때, [1, 3, 2, 4]에서 {3, 2}는 inversion이며 따라서 해당 순열은 inversion의 갯수가 총 1개라 하자.
* 비교하는 규칙에 따른 inversion의 갯수가 0인 순열을 우리는 sort된 모음이라 부른다.
* 따라서 sort는 기존의 객체들의 모음을 비교 규칙에 맞추어 재배열하는 과정을 통해 inversion의 갯수가 0이 되도록 만드는 일련의 과정이라 말할 수 있다.

## HeapSort

* 발전된 형태의 SelectionSort. 이유는 매번 정렬된 배열을 가지고 있고, 그 다음 위치에 존재할 값을 heap이라는 자료구조에서 찾아내는 과정을 반복하기 때문.
* Heap: array를 사용해서 저장할 경우 binary tree와 같이 left, right child를 가지고 있음. 좌측의 idx는 2 * parent_idx, 우측은 2 * parent_idx + 1
* max_heapify: heap에 포함 될 수 있는 최대 index 값과 정렬할 parent의 index를 주었을 때, 해당 지점으로부터 생성되는 sub_heap을 재정렬하는 연산.
* 최초에 array를 최대 index // 2의 instance부터 max_heapify를 수행하고, 점차적으로 더 작은 index에 대해서도 마찬가지를 진행한다. 최종적으로는 index 0에 대해 max_heapify를 수행하면 초기화가 완료된다.
  * <span style="color:red;"> ex) max_heapify(array, len(array), len(array)//2 - 1)
* 모든 heap의 root instance는 이제 maximum 값인 것이 보장된다.
* array의 가장 끝 instance와 root instance를 swap한다. 이러면 가장 큰 값으로부터 작아지는 정렬된 배열이 생성된다.
* heap의 size, 혹은 max_index 값을 decrement하고 현재 heap의 root에 대한 max_heapify를 재진행한 뒤, 전단계를 반복하면 Heapsort가 완성된다.