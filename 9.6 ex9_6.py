class dogs:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dogs(self):
        print("my_dog의 이름은 {}이고, 나이는 {}살입니다.".format(self.name,self.age))

my_dog = dogs("망고",3)
my_dog.dogs();