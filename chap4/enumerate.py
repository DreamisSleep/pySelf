# enumerate() 함수와 리스트

# 변수 선언
example_list = ["요소A", "요소B", "요소C"]

# 출력
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수 적용 후 출력
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환 후 출력
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerat() 함수 조합 사용
print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    # enumerate() 함수를 사용하면 반복 변수를 이런 형태로 넣을 수 있다.
    # i, value in enumerate(~~)
    print("{}번째 요소는 {}입니다.".format(i, value))