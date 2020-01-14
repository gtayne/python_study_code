class Geese:
    neck = "脖子较长" ##类属性，脖子
    wing = "振翅频率高" ###类属性，翅膀
    leg = "腿位于身体的中心支点" ##类属性，表示腿
    number = 0
  #  def __init__(self,beak,wing,claw): #self必须作为第一个参数，表示指向实例本身的引用定义 构造方法
    def __init__(self):
        Geese.number += 1 ##将编号加一
        print("\n我是第%d只大雁类"%Geese.number)
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)
  #      print(beak)                         #只能有一个构造方法
  #      print(wing)
  #      print(claw)


beak_1 = "喙"
wing_1 = "翅"
claw_1 = "爪"
#wildgoose = Geese(beak_1,wing_1,claw_1)
wildgoose = Geese()
#wildgoose.fly("飞行") ##调用实例方法
#wildgoose.fly()
list1 = []
for x in range(4):
    list1.append(Geese()) ###创建大雁类的实例
print("一共有%d只大雁"%Geese.number)
Geese.beak  = "喙的基部较高"  ###添加一个类属性
print(list1[3].beak)
