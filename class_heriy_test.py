# class Fruit:
#     def __init__(self,color = "green"):
#         Fruit.color = color
#     def harvest(self,color):
#         print("水果的默认颜色为",self.color)
# class Apple(Fruit):
#     color = "red"
#     def __init__(self):
#         print("我是苹果")
#         super.__init__(self)
# class Sapodilla(Fruit):
#     def __init__(self):
#         print("我是人参果")
#         super.__init__(self)
#     def harvest(self,color):
#         print("人参果是"+ Fruit.color ,"颜色的")
# apple = Apple
# apple.harvest(Apple.color)
# sapodilla = Sapodilla
# Sapodilla.harvest("gold yellow")
class Fruit:
    def __init__(self,color = "绿色"):
        Fruit.color = color
    def harvest(self, color):
        print("水果是" + self.color + "的")
        print("水果已经收获")
        print("水果原来是" + Fruit.color + "的！")
class Apple(Fruit):
    color = "红色"
    def __init__(self):
        print("我是苹果")
        super().__init__()
class Sapodilla(Fruit):
    def __init__(self,color):
        print("\n我是人参果")
        super().__init__(color)
    def harvest(self, color):
        print("人参果是" + color + "的")
        print("人参果已经收获")
        print("人参果的颜色是" + Fruit.color + "的")
apple = Apple()
apple.harvest(apple.color)
sapodilla = Sapodilla("白色")
sapodilla.harvest("金黄色")



