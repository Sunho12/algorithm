import sys
input = sys.stdin.readline

def fibonacci(n):
    zeros = [1,0,1]
    ones = [0,1,1]

    if n >= 3:
        for i in range(2, n):
            zeros.append(zeros[i]+zeros[i-1])
            ones.append(ones[i]+ones[i-1])
        
    print(f"{zeros[n]} {ones[n]}")


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        fibonacci(n)