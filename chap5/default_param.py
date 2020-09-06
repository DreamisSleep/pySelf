# 기본 매개변수
# 기본 매개변수 뒤에는 일반 매개변수가 올 수 없다
def print_n_times(value, n):
    # n번 반복합니다.
    for i in range(n):
        print(value)

# 함수 호출
print_n_times("안녕하세요")