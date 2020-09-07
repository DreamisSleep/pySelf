# 가변 매개변수 함수

def print_n_times(n, *values):
    # *values 는 가변 매개변수
    # print() 함수와 같이 매개변수를 원하는 만큼 받을 수 있는 함수
    # n번 반복
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        # 줄바꿈
        print()

# 함수 호출
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
