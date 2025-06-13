# day02

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    result=0
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for h in range(i, i+M):
                for k in range(j,j+M):
                    total += array[h][k]
            if total > result:
                result = total
    print(f"#{t} {result}")