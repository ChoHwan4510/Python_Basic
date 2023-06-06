'''
########기본 자료형##########
'''
#int : 정수
#float : 실수
#bool : 논리
#str : 문자열

#문자열 인덱싱
str = "HELLO"
str[0] # >> "H"
str[-1] # >> "O"

#문자열 슬라이싱
#s[start:stop:step]
#start : 시작 인덱스
#stop : 종료 인덱스
#step : 증감값
str[0:3] # >> "HEL"
str[0:4:2] # >> "HL"

'''
###########컬렉션###########
'''
#list : 추가,수정,삭제 가능 (array)
#tuple : 생성되고 나면 변경 불가능 (array)
#set : 중복저장 불가능, 인덱스가 없다 (object)
#dict : key+value로 관리 (object)
listValues = [1,2,3]
tupleValues = (1,2,3)
setValues = {1,2,3}
dictValues = {"key":"value"}



### list ###
#선언
listValues = [1,2,3]
listValues = list("반복가능객체")

#리스트 인덱스/슬라이싱
#문자열 슬라이싱과 동일
listValues[0] # >> "1"
listValues[0:1] # >> "[1,2]"

#리스트 요소의 추가와 삭제
#추가
listValues.append(500) # >> [1,2,3,500]
listValues.insert(1,90) # >> [1,90,2,3]
#삭제
listValues.pop() # >> 3, [1,2,3]
listValues.pop(0) # >> 1, [2,3]



### tuple ###
#선언
tupleValues = (1,2,3)
tupleValues = 1,2,3
tupleValues = tuple("반복가능객체")
tupleValues[0] # >> 1
#주의 튜플은 값을 1개만 보관시에 ,(콤마)를 찍어줘야한다
tupleValues = (1,)
tupleValues = 1,



### set ###
#선언
set = {1,2,3}
set = set("반복가능객체")
#중복값을 넣을수없다
set = {1,2,3,3,3,3,} # >> {1,2,3}
#리스트 중복 제거 응용
notDupleList = list(set([1,2,3,4,4,4,4,])) # >> [1,2,3,4]
#세트는 값을 추출할수 없어 list혹은 tuple로 변환후 값을 추출해야함

#세트 요소의 추가와 삭제
#추가
setValues = {1,2,3}
setValues.add(30) # >> {1,30,3,2} 저장되는 순서가 없음
#삭제
setValues.remove(2) # 2값이 없으면 KeyError 발생
setValues.discard(2) #2값이 없어도 오류 발생 X



### dictionary ###
#선언
dict = {"key":"value", "key2":"value2"}
dict["key"] # >> value

#딕셔너리 요소의 추가와 삭제
#추가
dict = {"apple":"사과"}
dict["watermelon"] = "수박" # >> {"apple":"사과", "watermelon":"수박"}
dict.setdefault("watermelon","수박") # >> print(dict.setdefault("orange","수박")) "수박" 추가된값을 반환한다
#수정
dict["watermelon"] = "멜론" # >> {"apple":"사과", "watermelon":"멜론"}
dict.update(watermelon="멜론")
#존재하지 않는 키값을 update할시에 새로운값으로 추가가된다 이경우 키가 문자열이 되어야한다
#삭제
dict.pop('apple') # >> {}



