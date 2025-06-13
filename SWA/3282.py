# day02

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    check_list = [0] * (K+1)

    for i in array:
        a = i[0]
        b = i[1]
        for j in range(K, a-1, -1):
            if check_list[j] < check_list[j-a] + b:
                check_list[j] = check_list[j-a] + b

    print(f'#{t + 1} {check_list[K]}')