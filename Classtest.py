#class Geese:
#    neck="脖子较长"
#    def __init__(self):
#        print(Geese.neck)
#Geese.beak="喙的属性"
#print(Geese.beak)
'''实例属性'''
'''
class Geese:
    def __init__(self):
        self.neck = "脖子较长"  #实例属性
        self.wing = "翅膀较宽"  #实例属性
        print(self.neck,self.wing,end="\n")
geese = Geese()  ###实例化类的对象
geese1 = Geese()
geese1.leg = "腿比较长"
print(geese1.leg) ##腿比较长
print(geese.wing) ###可以通过类的实例名称访问
print(Geese.wing) ###不可以通过类的名称访问AttributeError: type object 'Geese' has no attribute 'wing'

'''
'''访问限制'''
'''
class Geese:
    __neck_swan = "天鹅的脖子很长" ##定义私有类型属性
    def __init__(self):
        print("在构造方法中输出",Geese.__neck_swan) ###访问私有类型的属性
    def my(self):
        print("my方法", Geese.__neck_swan)  ###访问私有类型的属性
swan = Geese() ###创建Geese的实例（对象）
swan.my()   ###my方法 天鹅的脖子很长
swan._Geese__neck_swan = "脖子很长" ###修改私有类型属性
#print("直接访问",Geese.__neck_swan) ###通过实例名访问私有类型的属性,这种方法不可行
print("直接访问",swan._Geese__neck_swan) ###实例_类名__属性 可以访问私有属性
'''
'''@property'''
'''
class Rect:
    def __init__(self,width,height):  ###构造方法
        self.width = width ###定义实例属性
        self.height = height
    @property
    def area(self):
        return self.width*self.height ##计算矩形面积
rect = Rect(800,600)
print("面积为",rect.area)   ###输出面积
'''
class TVshow:
    list_film = ["武林外传","亮剑","三国","西游记"]
    def __init__(self,show):
        self.__show = show
    @property
    def show(self):
        return self.__show  ###返回私有属性
    @show.setter ###转变为可以修改
    def show(self,value):
        if value in TVshow.list_film: ###判断值是否在列表中
            self.__show = "您选择了" + value + "稍后将播放"  ###修改返回的值
        else:
            self.__show = "您点播的电影不存在"

print("您可以从",TVshow.list_film)
i = str(input())
tvshow = TVshow(111) ###创建类的实例
tvshow.show = i
print(tvshow.show)
#tvshow.show = TVshow("亮剑") ##@property 私有属性不可以修改 为只读属性
#print("默认",tvshow.show) ##获取属性值
