# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        for person in sorted(people, key=lambda x: int(x[2])):
            yield f(person)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

# input은 다음과 같이 주어진다
# 사람 이름 / 나이 / 성별
# 이를 나이 순으로 정렬하고, 각각의 사람 이름을 Mr. 또는 Ms.로 붙여서 반환하라.
if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')