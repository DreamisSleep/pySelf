# 범위
"""
첫째, 매개변수에 숫자를 한 개 넣는 방법
range(A)                         A는 숫자
0부터 A-1까지의 정수 범위

range(A, B)

range(A, B, C)
A부터 B-1까지의 정수 범위, 앞뒤의 숫자 C 만큼의 차이
"""
# for 반복문: 범위와 함께 사용
"""
for 숫자변수 in 범위:
    코드
"""

for i in range(5):
    # print( 숫자, 문자)
    print( i ,"= 반복 변수")
print()

for i in range(5, 10):
    # 문자열 + 문자열
    print(str(i) + "= 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + "= 반복 변수")
print()

# str() 변수에 숫자를 문자열로 저