T = int(input())

for i in range(T):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    speed = 0
    distance = 0

    for j in range(N):
        if array[j][0] == 1:
            speed += array[j][1]
            distance += speed
        elif array[j][0] == 2:
            speed -= array[j][1]
            # 차후에 속도가 음수일 때도 생각해보기
            if speed < 0:
                speed = 0
            distance += speed
        else:
            distance += speed

    print(f'#{i+1} {distance}')
