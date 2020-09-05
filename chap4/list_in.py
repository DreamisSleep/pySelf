# 리스트 안에 for문 사용

# 리스트 선언
array = [i * i for i in range(0, 20, 2)]
        # 최종 결과를 앞에 작성
"""
range(0, 20, 2)의 요소를 i라고 할 때 i*i로 리스트를 재조합하는 코드

를 리스트 내포(list comprehensions)라고 함

리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]
"""

# 출력
print(array)
