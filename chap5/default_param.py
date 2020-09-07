# 기본 매개변수
# 기본 매개변수 뒤에는 일반 매개변수가 올 수 없다
# 기본 매개변수가 가변 매개변수 앞에 써도 의미가 없다.
# 가변 매개변수가 기본 매개변수보다 앞에 와도 다르다.
def print_n_times(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)

# 함수 호출
print_n_times("안녕하세요")