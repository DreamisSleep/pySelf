# 조건을 활용한 리스트 내포

# 리스트를 선언
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
"""
array의 요소를 fruit이라고 할 때 초콜릿이 아닌 fruit으로 리스트를 재조합

실행함년 초콜릿을 제외한 요소만 모인 리스트를 만든다
if구문을 포함한 리스트 내포는 다음과 같은 형태로 사용

리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
"""

# 출력
print(output)