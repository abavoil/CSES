def main():
    n = int(input())
    while n != 1:
        print(n, end=" ")
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    print(1)


if __name__ == '__main__':
    main()
