import random

class Hat:
    houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

    @classmethod
    # cls是class的简写防止冲突
    def sort(cls, name):
        print(name,"is in",random.choice(cls.houses))

# 无需创建多个实例
Hat.sort("Harry")