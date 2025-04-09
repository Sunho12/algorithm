import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    
    total_profit = 0 #이익
    max_price = 0

    for price in reversed(prices):
        if price > max_price:
            max_price = price
        total_profit += max_price - price

    print(total_profit)