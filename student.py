class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_values(self):
        print("-------------------")
        print("Name : "+self.name)
        print("Age :"+str(self.age))


students=[]

students.append(Student("arun",22))
students.append(Student("amal",23))
students.append(Student("aleena",20))

k=0
for i in students:
    print(students[k].get_values())
    k=k+1