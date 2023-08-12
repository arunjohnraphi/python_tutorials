class Student:
    def __init__(self,name ,age: int):
        self.name = name
        self.age = age

    def talk(self):
        print("hi,im " + self.name )

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

s1 = Student("arun", 24.2)

s2 = Student("amal", 24)

if s1.compare(s2):
    print ("they are same")
else:
    print ("they are different")