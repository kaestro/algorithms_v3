# Sample Problems that can be solved with BFS

해당 문제들을
* 왜 BFS를 사용해서 푸는지
* 판단 근거는 무엇인지
* 해결 과정은 어떻게 될 지

에 대해 고민해 보자

## 미로 찾기

주어진 2D 그리드에서 출발 지점에서 도착 지점까지의 최단 경로를 찾아야 합니다. 그리드는 벽으로 막혀있고, 출발 지점과 도착 지점은 열린 공간입니다. 각 칸은 이동 가능한 곳(0) 또는 벽(1)으로 표시되어 있습니다. 상하좌우로 인접한 이동만 가능하며, 벽을 통과하거나 대각선으로 이동할 수 없습니다.

## 나이트의 이동 (Knight's Tour)

체스판 위에 있는 나이트(나이트는 L자 형태로만 이동 가능)가 출발 지점에서 도착 지점까지 이동하는 최단 경로를 찾아야 합니다.

## 섬의 개수 (Number of Islands)

0과 1로 이루어진 2D 그리드가 주어집니다. 1은 땅을 나타내고, 0은 물을 나타냅니다. 이때 섬의 개수를 찾아야 합니다. 섬은 상하좌우 및 대각선으로 인접한 땅이 연결된 영역을 의미합니다.

## 커리큘럼 설계 (Curriculum Design)

대학에서 강의들은 선수 강의가 있을 수 있습니다. 각 강의는 일정한 시간이 소요되며, 선수 강의를 들었을 때에만 수강할 수 있는 강의들이 있습니다. 주어진 강의 정보와 선수 강의 정보를 바탕으로, 모든 강의를 수강하는 데 걸리는 최소 시간을 계산하는 문제입니다.

## 단어 변환 (Word Transformation)

문제 설명: 주어진 시작 단어에서 목표 단어로 변환하는 최소 단계를 찾아야 합니다. 단어는 한 번에 한 글자씩 변경될 수 있으며, 각 변경된 단어는 주어진 단어 리스트에 포함되어야 합니다.