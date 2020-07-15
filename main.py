import sys


def do():
    for line in sys.stdin:
        words = line.split()
        print(words[0])
        for i in range(1, len(words[0])):
            print(words[0][:-i])
        for i in range(2, len(words[1])):
            print(words[1][:i])
        print(words[1])


if __name__ == '__main__':
    do()



