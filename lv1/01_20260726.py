# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12912

# my code
def solution(a, b):
    answer = 0
    
    if a > b:
        answer = b
        for i in range(a-b):
            b += 1
            answer = answer + b
    elif b > a:
            answer = a
            for i in range(b-a):
                a += 1
                answer += a
    else:
        answer = a
    return answer


# 좋아보이는 코드
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))