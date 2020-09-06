# reversed() 함수와 이터레이터

# 변수 선언
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

# reversed_numbers 출력
print("reversed_numbers : ", r_num)
print(next(r_num)) # 이터러블 중 next()함수는 요소를 하나하나 꺼낼 수 있다
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))