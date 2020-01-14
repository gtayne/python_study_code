class Fruit:
    def __init__(self,color = "green"):
        Fruit.color = color ##类属性
    def harvest(self,color):
        print("水果是",color,"颜色的") ###输出形式参数color
        print("水果已经收货...")
        print("水果原来是",Fruit.color) ###输出类属性
class Apple(Fruit):
    color = 'red' ###类属性
    def __init__(self):
        print("我是苹果")
        super().__init__()  ###在派生类中调用基类的派生方法
        print(Fruit.color)
    def harvest(self,color): ###重写方法
        print("苹果是",color,"颜色的") ###输出形式参数color
        print("水果已经收货...")
        print("水果原来是",Fruit.color) ###输出类属性
#class oragne(Fruit):
#    color = 'orange' ###类属性
#    def __init__(self):
#        print("我是橙子")
#    def harvest(self,color): ###重写方法
#        print("橘子是",color,"颜色的") ###输出形式参数color
#        print("水果已经收货...")
#        print("水果原来是",Fruit.color) ###输出类属性

apple = Apple() ###创建子类的实例
apple.harvest(apple.color)  ###调用父类的方法
oragne = oragne()
oragne.harvest(oragne.color)
