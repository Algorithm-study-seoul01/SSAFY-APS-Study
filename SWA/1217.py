# day03

T = 10

for t in range(1, T+1):
    test_num = int(input())
    N,M = map(int, input().split())
    
    result = N**M
    
    print(f'#{test_num} {result}')