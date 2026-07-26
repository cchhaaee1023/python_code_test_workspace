# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12909

#my
def solution(s):
    #리스트 형태로 변환
    li_str = list(s)

    # 기본적 조건 실패경우
    if li_str[0] != '(':
        return False  # 시작은 무조건 '(' 이어야 함
    elif li_str[len(s) - 1] != ')':
        return False        #문자열 끝은 무조건 ')' 아니면 False
    
    count_left = 0
    count_right = 0
    
    for i in li_str:
        if i == '(':
            count_left += 1
        elif i == ')':
            count_right += 1
        if count_right > count_left:        #오른쪽 괄호가 먼저 나온 경우
            return False
        
    return count_left == count_right


# 스택, 큐 문제..
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0