import sys

class Student:
    def __init__(self,name,house):
        self.name = name
        #trigger the decorator "setter"
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            #主动抛出异常
            raise ValueError("Missing name")
        self._name = name


    @property
    def house(self):
        #Advanced setting 避免重名
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise TypeError("Invalid house") 
        #_house只用来检验，不用来存值
        self._house = house

    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house: ")
        return cls(name, house)
        

def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
