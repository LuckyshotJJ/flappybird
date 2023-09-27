class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hi(self):
        print(f"你好我是{self.name}")


class Student(Person):        #繼承把Person所有的程式碼複製一份到Student
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)     #引入Person初始函式
        self.score = score
s1 = Student("小白", 23, 70)
print(s1.name)
print(s1.age)
print(s1.score)
s1.say_hi()