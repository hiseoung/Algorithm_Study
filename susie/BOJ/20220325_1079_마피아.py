import sys
input = sys.stdin.readline

N = int(input())
guilt = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
my_pos = int(input())
dead = [0] * N
dead_cnt = 0
answer = 0

def solution(cnt, day):
    global N, my_pos, answer, dead_cnt

    if cnt > answer:
      answer = cnt
    
    #마지막까지 내가 생존했을 경우
    if dead_cnt == N-1:
        return

    #낮
    if day:
        idx = 0
        guilt_point = 0
        for i in range(N):
            #안죽은 사람들만 유죄 지수 탐색
            if dead[i] == 0:
                #생존자들 중 가장 큰 유죄 지수를 탐색
                if guilt[i] > guilt_point:
                    guilt_point = guilt[i]
                    idx = i
        #내 유죄지수가 생존자들중 가장 큰 경우
        if idx == my_pos:
            return
        
        #밤으로
        dead[idx] = 1
        day = 0
        dead_cnt += 1
        solution(cnt, day)

        dead_cnt -= 1
        day = 1
        dead[idx] = 0

    #밤
    else:
        for i in range(N):
            #생존자이면서 내가 아닌 다른 사람을 죽일 경우
            if dead[i] == 0 and i != my_pos:
                dead[i] = 1
                #죽일 사람의 유죄지수를 더한다
                for j in range(N):
                    guilt[j] += arr[i][j]
                
                #낮으로
                cnt += 1
                day = 1
                dead_cnt += 1
                solution(cnt, day)

                dead_cnt -= 1
                dead[i] = 0
                day = 0
                cnt -= 1
                for j in range(N):
                    guilt[j] -= arr[i][j]

#인원 홀수시 낮부터 시작, 짝수일 경우 밤부터 시작
if N % 2 == 1:
    solution(0, 1)
else:
    solution(0, 0)

print(answer)
