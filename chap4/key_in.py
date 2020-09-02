# 키가 존재하는지 확인하고 값에 접근하기

# 딕셔너리 선언
dictionary = {
    "name": "건조 망고",
    "type": "당절임",
    "ingredient": ["1", "2", "3", "4"],
    "origin": "필리핀"  
}

# 사용자로부터 입력을 받기
key = input("> 접근하고자 하는 키: ")

# 출력
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")
