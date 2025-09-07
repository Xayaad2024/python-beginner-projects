
class student:
    school_name = "decac school"
    def __init__(self,name):
        self.name =  name
    @classmethod
    def change_school(cls,new_name):
        cls.school_name = new_name

    def show(self):
        print(f"{self.name} studies at {student.school_name}")

s1 = student("ali")
s2 = student("sara")
s1.show()
s2.show()

#changing class variable class name
student.change_school("kole secondary school.")

s1.show()
s2.show()