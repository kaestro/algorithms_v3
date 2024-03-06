# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    basic_list = []

    N = int(input())

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            basic_list.insert(int(command[1]), int(command[2]))

        elif command[0] == "print":
            print(basic_list)

        elif command[0] == "remove":
            if int(command[1]) in basic_list:
                basic_list.remove(int(command[1]))

        elif command[0] == "append":
            basic_list.append(int(command[1]))

        elif command[0] == "sort":
            basic_list.sort()

        elif command[0] == "pop":
            basic_list.pop()

        elif command[0] == "reverse":
            basic_list.reverse()