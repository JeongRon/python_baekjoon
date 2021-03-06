"""
2292 - 벌집 (브론즈 2)
"""

N = int(input())

if N == 1:
    print(1)
else:
    N -= 1
    a = 1
    b = 6
    cnt = 2
    while True:
        if a <= N <= b:
            print(cnt)
            break
        a = b + 1
        b += 6 * cnt
        cnt += 1

# review
# 입력 : 1 / 2~7 / 8~19 / 20~37 / ...
# 출력 : 1 / 2   / 3    / 4     / ...
# 문제 이해 과정에서 6의 배수랑 연관 있다고 생각
# 입력 받은 것을 -1 하면, 1~6 / 7~18 / 19~36 .. 으로 맨 뒤에가 6의 배수
# 최소 최대값 a 와 b를 지정하고 a,b 사이에 N의 값이 있으면 cnt를 출력하게끔 코드 작성
