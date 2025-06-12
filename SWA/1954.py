T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # 델타
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = j = k = 0 # i, j, k = 0이랑 헷갈리지 않기

    for num in range(1, N * N + 1):
        arr[i][j] = num
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            k = (k + 1) % 4
            i += di[k]
            j += dj[k]

    print(f'#{t}')
    for E in arr:
        print(*E)
