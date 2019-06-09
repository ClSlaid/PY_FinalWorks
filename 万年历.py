import tkinter,time
from turtle import *

def Skip(step):
	penup()
	forward(step)
	pendown()

def mkHand(name, length):
	#注册Turtle形状，建立表针Turtle
	reset()  #清空当前窗口，并重置位置等信息为默认值
	Skip(-length*0.1)
	begin_poly()
	forward(length*1.1)
	end_poly()
	handForm = get_poly()
	register_shape(name, handForm) 

def Init():
	global secHand, minHand, hurHand, printer#建立三个指针和输出文字turtle
	mode("logo")# 重置Turtle指向北
	#建立三个表针Turtle并初始化
	mkHand("secHand", 135)
	mkHand("minHand",  110)
	mkHand("hurHand", 90)
	secHand = Turtle()
	secHand.shape("secHand")
	minHand = Turtle()
	minHand.shape("minHand")
	hurHand = Turtle()
	hurHand.shape("hurHand")
	for hand in secHand, minHand, hurHand:
		hand.shapesize(1, 1, 3)
		hand.speed(0)
	#建立输出文字Turtle
	printer = Turtle()
	printer.hideturtle()
	printer.penup()
     
def SetupClock(radius):
	# 绘制表的外框，通过取余来绘制表盘刻度
	reset()
	pensize(7)
	for i in range(60):
		Skip(radius)
		if i % 5 == 0:
			forward(20)
			Skip(-radius - 20)
			
			Skip(radius + 20)
			if i == 0:
				write(int(12), align="center", font=("Courier", 14, "bold"))
			elif i == 30:
				Skip(25)
				write(int(i/5), align="center", font=("Courier", 14, "bold"))
				Skip(-25)
			elif (i == 25 or i == 35):
				Skip(20)
				write(int(i/5), align="center", font=("Courier", 14, "bold"))
				Skip(-20)
			else:
				write(int(i/5), align="center", font=("Courier", 14, "bold"))
			Skip(-radius - 20)
		else:
			dot(5)
			Skip(-radius)
		right(6)
		 

def leap_year(year):#计算闰年
	
	if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
		return "闰年"
	else:
		return "不是闰年"
        
def lunar_year(year):#计算干支年和年的属相
	T='甲乙丙丁戊己庚辛壬癸'
	D='子丑寅卯辰巳午未申酉戌亥'
	S='鼠牛虎兔龙蛇马羊猴鸡狗猪'
	n=year-1984
	while n<0:
		n=n+60
	return T[n%10]+D[n%12]+S[n%12]+'年'+'	'


def Tick(t):
    #绘制表针的动态显示
	second = t[-1]
	minute = t[-2] + second/60.0
	hour = t[-3] + minute/60.0
	secHand.setheading(6*second) #设置朝向，每秒转动6度
	minHand.setheading(6*minute) 
	hurHand.setheading(30*hour)
	nowtime=str(t[0])+'年'+str(t[1])+'月'+str(t[2])+'日'+str(t[3])+'时'+str(t[4])+'分'+str(t[5])+'秒'
	tracer(False)  #不显示绘制的过程，直接显示绘制结果
	printer.forward(65)
	printer.write("时钟", align="center",
				font=("Courier", 14, "bold"))
	printer.back(130)
	printer.write(nowtime, align="center",
				font=("Courier", 14, "bold"))
	printer.back(50)
	tracer(True)
	time.sleep(1)
	printer.clear()
	printer.write(lunar_year(t[0])+leap_year(t[0]), align="center",
			font=("Courier", 14, "bold"))
	printer.home()



def showtime(t):
	tracer(False) #turtle实现时钟图形
	Init()
	SetupClock(160)
	tracer(True)
	while True:#一秒刷新一次
		Tick(t)
		t[-1]=(t[-1]+1)%60
		if t[-1]==59:
			t[-2]=(t[-2]+1)%60
		if t[-2]==59:
			t[-3]=(t[-3]+1)%12
	mainloop()


def main():
	t=[]
	choice=input('已经获取当前时间，是否要设置钟表时间？（Y for yes |N for no）\n')
	
	if choice=='Y':
		print('输入修改的时间(年月日时分秒)')
	
		for i in range(6):
			temp=int((input()))
			t.append(temp)
		print('基于输入的时间的时钟绘制完毕')
		showtime(t)
	
	elif choice=='N':
		t = list(time.localtime())[:6]#t存储当前时间
		print('基于当前时间的时钟绘制完毕')
		showtime(t)
	
	else :
		print('输入错误！\n')



if __name__ == "__main__":
    main()
