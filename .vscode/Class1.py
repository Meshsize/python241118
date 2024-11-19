# Class1.py
# 1) 클래스 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "Default Name"
    def print(self):
        print("My name is {0}".format(self.name))

# 2) 인스턴스 실행
p1 = Person()
p2 = Person()

p1.name = '조원'
p1.print()

p2.name = '최나래'
p2.print()


#전역변수
strName = '전역변수의 값'
class DemoString:
    def __init__(self):
        self.name('')