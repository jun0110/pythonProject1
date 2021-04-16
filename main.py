# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 리스트
x = list()
y = ["hello", "world"]
z = ["hello", 1, 2, 3]

print(x+y)

# 0부터 시작
print(y[0])
# 수정
z[3] = 100
print(z)

# 리스트 사이즈알기 len
x = [1,2,3,101,100,4]

num_elements = len(x)
print(num_elements)

# 정렬하기 sorted(숫자만)
n= sorted(x)
print(n)

# 합치기 sum(숫자만가능)
b = sum(x)
print(b)

# 위치찾기index
print(x.index(3))
print(y.index("hello"))

# 존재유무 ("찾는값" in 리스트)
print("hello" in y)
if "hello" in y:
    print("Hello 가 있어요")
# for문 예제
for n in x:
    print(n)

# 튜플 밑에 두개처럼 만들 수 있고 대괄호 대신 소괄호 가능
x = tuple()
y= ()

x = (1, 2, 3)
y = ('a', 'b', 'c')
# 리스트에서 썻던 펑션 그대로사용가능
print(x+y)
print('a' in y)
print(z.index(1))

# 튜플에서는 assignment 안됌 업데이트불가
# 리스트 imutable 튜플immutable
# x[0]= 10 안됌

# 딕셔너리 두가지방법 만들기가능
# 키와(불변값만들어감(문자열이나 숫자)
# 벨류로 이루어져있음
x = dict()
y={}

x = {
    "name": "워니",
    "ㅁㅎㄷ": 20,
}

print(x["name"])
print(x["ㅁㅎㄷ"])

# 리스트와 마찬가지로 어떤키가있는지 알 수 있음
print("name" in x)

# x.key() 딕셔너리 모든키 보기
print(x.keys())
# x.values() 딕셔너리 모든 벨류 보기
print(x.values())

# 딕셔너리 엘리먼트 돌아보기
for key in x:
    print(key)
    print(x[key])
# 새로운 값 넣을때
x[0] = "nana"
print(x)
# 키 값의 벨류 교체할때
x["name"]="워워"
print(x)

# 해볼거 과일 숫자 프로그램짜기
fruit = ["사과", "사과", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

print(fruit)

d = {}

for n in fruit:
    if n in d:
        d[n] = d[n] + 1

    else:
        d[n] = 1

print(d)

# 클래스 함수랑 변수들의 합
# 오브젝트 : 클래스를 이용해서 만들어낸거
# 클래스는 빵틀 빵틀로찍어낸빵 = 오브젝트 =인스턴스

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! 나는" + to_name + "나는" + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")


class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다. " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지?" + to_program)

wonie = Person("워니", 20)
jenny = Police("제니", 21)
michael = Programmer("마이클" , 22)

jenny.arrest("워니")

# 패키지(파이썬에서는 이렇게부름) = 라이브러리 = 모듈들의 합
# 모듈=코드를 모아 기능하는 파일

# animal package
# dog, cat modules
# dog, cat modules can say "hi"

# 패키지 만들려면 폴더 만들고 폴더의 이름이 패키지이름


from animal import dog # animal 패키지에서 dog 모듈 가져와줘
from animal import cat

d = dog.Dog() # instance
d.hi()

c = cat.Cat()
c.hi()

from animal import * # 이걸쓰면 파일지정 안해도댐
d = Dog()
c = Cat()

d.hi()
c.hi()



from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Jun")
location = geolocator.geocode("Busan, South Korea")

print((location.latitude, location.longitude))


# twilio.com
# +12406680213
# AC33dd010b30eddc7c2c1811c55227ca89
# 986b031ed7c86c412560f2e94f4bc5b5
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client



# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC33dd010b30eddc7c2c1811c55227ca89'
auth_token = '986b031ed7c86c412560f2e94f4bc5b5'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="ㅎㅎ 문자성공",
                     from_='+12406680213',
                     to='+8201022206384'
                 )

print(message.sid)