def main():
    n = int(input())
    numbers = set(range(1, n + 1))
    for i in map(int, input().split()):
        numbers.remove(i)
    print(numbers.pop())


if __name__ == '__main__':
    main()
