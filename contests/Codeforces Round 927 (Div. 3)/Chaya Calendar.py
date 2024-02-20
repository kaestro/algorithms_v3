# periodicity는 해당 숫자가 나타나는 주기를 의미한다.
# 해당 주기가 ith 수일 경우, 해당 수를 i배 한 수 중 가장 작은 값이 현재이다.
def apocalypse_year(periodicities: list[int]) -> int:
    current_year = 0
    for periodicity in periodicities:
        next_year = periodicity
        while next_year <= current_year:
            next_year += periodicity
        current_year = next_year

    return current_year

def main():
    t = int(input())
    list_periodicities = []
    for _ in range(t):
        num = input()
        list_periodicities.append(list(map(int, input().strip().split())))

    for periodicities in list_periodicities:
        print(apocalypse_year(periodicities))

if __name__ == "__main__":
    main()