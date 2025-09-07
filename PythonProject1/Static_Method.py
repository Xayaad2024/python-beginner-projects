class mathUtils:
    @staticmethod
    def add(a,d):
        return a+d
    @staticmethod
    def multiply(c,b):
        return c*b
# call static method without creating an object.
print(mathUtils.add(34,2))
print(mathUtils.multiply(5,4))