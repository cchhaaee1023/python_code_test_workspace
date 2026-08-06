# https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    li = [i for i in range(1, n+1) if n % i == 0]
    answer = sum(li)
    return answer