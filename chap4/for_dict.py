"""
for 키변수 in 딕셔너리:
    코드
"""

# for 반복문과 딕셔너리

# 딕셔너리 선언
dictionary = {
    "name": "건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메아중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# for 반복문을 사용
for key in dictionary:
    # 출력
    print(key, ":", dictionary[key])