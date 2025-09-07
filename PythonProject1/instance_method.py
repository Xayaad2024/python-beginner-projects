class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # instance method
    def greet(self):
        print(f" hello my name is {self.name} and i am {self.age} years old.")

    # creating an instance
s1 = student("Ali",20)
s2 = student("dataa",26)
s3 = student("axmed",30)
s4 = student("seytuun",24)
s1.greet()
s2.greet()
s3.greet()
s4.greet()