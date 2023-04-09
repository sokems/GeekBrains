import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    t = read_int()
    for _ in range(t):
        n = read_int()
        a = sorted(read_ints())
        r = a[0] ^ a[1]
        for i in range(1, n):
            r = min(r, a[i - 1] ^ a[i])

        print(r)

main()