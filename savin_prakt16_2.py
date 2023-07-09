class Turtle(object):
    x=0
    y=0
    s=0
    x2=0
    y2=0

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.s=0
        self.vyvod(self.x, self.y,self.s)

    def vyvod(self,x,y,s):
        print("Текущие координаты",self.x, self.y,", скорость",self.s)
        if (x2==self.x) and (y2==self.y):
            print("Вы на месте!\n")
        else:
            print("До цели:",x2-self.x,"клеток по X,",y2-self.y,"клеток по Y\n")

    def go_up(self):
        self.y+=self.s
        self.vyvod(self.x, self.y,self.s)
        
    def go_down(self):
        self.y-=self.s
        self.vyvod(self.x, self.y,self.s) 
        
    def go_left(self):
        self.x-=self.s
        self.vyvod(self.x, self.y,self.s)
        
    def go_right(self):
        self.x+=self.s
        self.vyvod(self.x, self.y,self.s)
        
    def evolve(self):
        self.s+=1
        self.vyvod(self.x, self.y,self.s)
        
    def degrade(self):
        self.s-=1
        if self.s<=0:
            print("Нельзя уменьшать скорость до 0 и ниже")
            self.s+=1
        self.vyvod(self.x, self.y,self.s)

    def count_moves(self,x1,y1,x2,y2):
        tmp1=abs(x2-self.x)
        tmp2=abs(y2-self.y)
        print("Минимальное количество действий:",tmp1+tmp2+1)
        print("В том числе:")
        print("Одно увеличение скорости")
        print(tmp1," движений по оси Х")
        print(tmp2," движений по оси Y\n")
    
# -----------------------------
command=""

print("Введите начальные координаты через пробел (скорость по умолчанию 0)")
x,y=map(int,input().split())
print("Введите координаты цели через пробел")
x2,y2=map(int,input().split())

My_Turtle=Turtle(x,y)
My_Turtle.count_moves(x,y,x2,y2)

while command!="stop":
    print("Введите команду (up,down,left,right,evolve,degrade), stop для выхода")
    command=input()
    if command=="up":
        My_Turtle.go_up()
    elif command=="down":
        My_Turtle.go_down()
    elif command=="left":
        My_Turtle.go_left()
    elif command=="right":
        My_Turtle.go_right()
    elif command=="evolve":
        My_Turtle.evolve()
    elif command=="degrade":
        My_Turtle.degrade()
