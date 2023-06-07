'''
####### 이스케이프 #######
'''
#\' : 작은따옴표
#\" : 큰따옴표
#\n : 줄 바꿈
#\r : 캐리지 리턴
#\t : 탭(tab)
#\\ : 역슬래시(\)
#\b : 백스페이스

### print()함수 ###
#print(value, sep=' ', end='\n')
#sep = value의 구분자
#end = value 출력후 출력할 문자
print("Hello python World") #>> Hello python World
print("Hello", "python", "World", sep="|") # >> Hello|python|World
print("HELLO",end="|||") # >> HELLO|||


'''
####### %연산자 #######
'''
#C or JAVA에서 동일하게 사용되는 출력방식
# %d : 정수(10진수)
# %f : 실수
# %s : 문자열
print("%d" %10) # >> 10
print("%f" %3.14) # >> 3.14 
print("%s" %'Python') # >> Python
print("%d %f %s" %(10, 3.14 ,"Python")) # >>10 3.14 Python


'''
####### format()메서드 #######
'''
#%연산자대신 유용하게 사용 {}을 사용
print("Blues Archive is {} Game {}".format("Perfect",1000)) # >> Blues Archive is Perfect Game 1000
print("Blues Archive is {0} Game {1}".format("Perfect",1000)) # >> Blues Archive is Perfect Game 1000
print("Blues Archive is {1} Game {0}".format("Perfect",1000)) # >> Blues Archive is 1000 Game Perfect
print("Blues Archive is {name} Game {number}".format(name="Perfect",number=1000)) # >> Blues Archive is Perfect Game 1000


'''
####### f-string #######
'''
#파이썬 3.6이후 사용가능 {} 안에 직접변수대입
who="소라사키 히나짱"
what="귀여워"
print(f"블루아카이브에 나오는 {who}는 {what}") # >> 블루아카이브에 나오는 소라사키 히나는 귀여워


'''
####### input()함수 #######
'''
# 키보드 입력 함수
# 받은값의 type은 String 이다
inputvalue = input("아무거나 입력하시오")
print(inputvalue) # >> 입력한 값
print(int(inputvalue)) # >>정수값을 받을때는 int함수로 형변환을 해줘야한다
print(float(inputvalue)) # >>실수값을 받을때는 float함수로 형변환을 해줘야한다





