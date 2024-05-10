# https://school.programmers.co.kr/learn/courses/30/lessons/250121

from typing import List

# data는 [[코드 번호, date, 최대 수량, 현재 수량], ...]으로 이루어진 2차원 배열이다.
# ext는 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열이다.
# ext에는 'code', 'date', 'maximum', 'remain' 중 하나의 값이 들어온다.
# val_ext는 ext에 따라 뽑아낸 데이터를 어떤 정수를 말한다.
# sort_by는 정렬 기준을 의미하는 문자열이다.

# data에서 ext 값이 val_ext 보다 작은 데이터만 뽑은 후,
# sort_by의 값에 따라 data를 오름차순 정렬하여 return하도록 구현하라.
def solution(datum: List[List], ext_codes: str, val_ext: int, sort_by: str)->List[List]:
    answer = []

    if ext_codes == 'code':
        ext_idx = 0
    elif ext_codes == 'date':
        ext_idx = 1
    elif ext_codes == 'maximum':
        ext_idx = 2
    else:
        ext_idx = 3
    
    for data in datum:
        if data[ext_idx] < val_ext:
            answer.append(data)
        
    if sort_by == 'code':
        sort_idx = 0
    elif sort_by == 'date':
        sort_idx = 1
    elif sort_by == 'maximum':
        sort_idx = 2
    else:
        sort_idx = 3
    answer.sort(key=lambda x: x[sort_idx])

    return answer