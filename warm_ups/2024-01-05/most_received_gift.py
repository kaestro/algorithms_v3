# https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3

def solution(friends, gifts):
    answer = 0

    # preprocessing
    gift_coefficients, gift_matrix = preprocessing(friends, gifts)

    new_gifts = {}
    for friend in friends:
        new_gifts[friend] = 0
    
    for giver, recipients in gift_matrix.items():
        for recipient, num_given in recipients.items():
            num_received = gift_matrix[recipient][giver]
            gift_diff = num_given - num_received

            if is_better_gift(gift_diff, gift_coefficients[giver], gift_coefficients[recipient]):
                new_gifts[giver] += 1
    
    max_friend = max(new_gifts, key=new_gifts.get)

    return new_gifts[max_friend]


def is_better_gift(gift_diff, coefficient_giver, coefficient_recipeint):
    if gift_diff > 0:
        return True
    elif gift_diff == 0 and coefficient_giver > coefficient_recipeint:
        return True
    return False

# returns gift coefficients, gift matrix
def preprocessing(friends, gifts):

    gift_matrix = {friend: {other_friend: 0 for other_friend in friends} for friend in friends}
    gift_coefficients = {friend: 0 for friend in friends}

    for gift in gifts:
        giver, recipient = gift.split()

        # 준 사람의 지수 값을 +1한다.
        # 받은 사람의 지수 값을 -1한다
        gift_coefficients[giver] += 1
        gift_coefficients[recipient] -= 1
        
        # gift_matrix에서 giver/recipient의 관계를 변환한다.
        gift_matrix[giver][recipient] += 1

    return gift_coefficients, gift_matrix


if __name__ == "__main__":
    friends_list = [
        ["muzi", "ryan", "frodo", "neo"],
        ["joy", "brad", "alessandro", "conan", "david"],
        ["a", "b", "c"],
    ]

    gifts_list = [
        ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi",
            "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"],
        ["alessandro brad", "alessandro joy", "alessandro conan",
            "david alessandro", "alessandro david"],
        ["a b", "b a", "c a", "a c", "a c", "c a"]
    ]

    answers_list = [2, 4, 0]





    for index in range(len(friends_list)):
        answer = solution(friends=friends_list[index], gifts=gifts_list[index])
        print(str(index) + "번째 데이터에 대한 당신의 함수는 " + str(answer) + "를 값으로 계산했습니다.")
        if  answer == answers_list[index]:
            print("정답입니다")
        else:
            print("오답입니다.")