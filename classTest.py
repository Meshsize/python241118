class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 1: Person 클래스 인스턴스 생성 및 정보 출력
p1 = Person(1, "Alice")
p1.printInfo()  # 예상 출력: ID: 1, Name: Alice

# 테스트 2: Manager 클래스 인스턴스 생성 및 정보 출력
m1 = Manager(2, "Bob", "Team Lead")
m1.printInfo()  # 예상 출력: ID: 2, Name: Bob, Title: Team Lead

# 테스트 3: Employee 클래스 인스턴스 생성 및 정보 출력
e1 = Employee(3, "Charlie", "Python Developer")
e1.printInfo()  # 예상 출력: ID: 3, Name: Charlie, Skill: Python Developer

# 테스트 4: 여러 Person 인스턴스 생성 및 정보 출력
p2 = Person(4, "Diana")
p2.printInfo()  # 예상 출력: ID: 4, Name: Diana

# 테스트 5: Manager 클래스 다른 인스턴스 생성 및 정보 출력
m2 = Manager(5, "Eve", "Project Manager")
m2.printInfo()  # 예상 출력: ID: 5, Name: Eve, Title: Project Manager

# 테스트 6: Employee 클래스 다른 인스턴스 생성 및 정보 출력
e2 = Employee(6, "Frank", "Data Analyst")
e2.printInfo()  # 예상 출력: ID: 6, Name: Frank, Skill: Data Analyst

# 테스트 7: Manager 클래스의 title 변경 후 출력
m1.title = "Senior Team Lead"
m1.printInfo()  # 예상 출력: ID: 2, Name: Bob, Title: Senior Team Lead

# 테스트 8: Employee 클래스의 skill 변경 후 출력
e1.skill = "Full Stack Developer"
e1.printInfo()  # 예상 출력: ID: 3, Name: Charlie, Skill: Full Stack Developer

# 테스트 9: Person 클래스 정보 출력 재확인
p1.printInfo()  # 예상 출력: ID: 1, Name: Alice

# 테스트 10: 모든 클래스 인스턴스를 리스트로 관리하고 반복 출력
people = [p1, m1, e1, p2, m2, e2]
for person in people:
    person.printInfo()
