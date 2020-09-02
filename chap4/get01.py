# get() 함수
# 키가 존재하지 않을 때 None을 출력하는지 확인하기

# 딕셔너리 선언
dictionary = {
    "name": "건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 존재하지 않는 키에 접근
value = dictionary.get("name")
print("값:", value)

# Nonde 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다")