from vpython import *
from time import sleep

#自定义函数
def make_color(r,g,b):
    return vec(r/255,g/255,b/255)#颜色就是rgb的向量

#场景
sc0 = canvas(
    width=1200,
    height=600,
    x=0,
    y=0,
    background=make_color(232,251,253),
    align="left",
    center=vec(40,5,0),
    range=25,
    autoscale=False,
    userspin=False,
    userspan=False)

#变量
mball = 10
vcar = vec(10,0,0)
vproj = vec(-10,10*sqrt(3),0)
vball0 = vcar+ vproj
g = vec(0,-9.8,0)
t = 0
dt = 0.02
throwed = False
running = False
inputcontent = None

#对象
car = box(pos=vec(0,0,0),size=vec(10,5,0.1),axis=vec(1,0,0),color=color.red)
ball0 = sphere(pos=car.pos - vec(5,-2.5,0),radius=1,color=color.cyan)
bgcube = box(pos=vec(0,0,0),size=vec(2,20,0.1),axis=vec(1,0,0),visible=False,color=color.white)#竖直轨迹条
VecVcar = arrow(pos=car.pos,axis=vec(10,0,0),color=make_color(117,249,77))
VecVball0 = arrow(pos=ball0.pos,axis=vec(6,0,0),color=make_color(50,130,246))
VecVball1 = arrow(pos=ball0.pos,axis=vec(-3,3*sqrt(3),0),color=make_color(240,134,80))
Vcartext = label(pos=VecVcar.pos+vec(0,3,0),text="v=10m/s",color=vec(0,0,0))

#菜单
##暂停按钮
def pause(button):
    global running
    running = not running
    if running:
        button.text = "Pause"
        resetButton.disabled = True
        
        projangSlider.disabled = True
        prospbox.disabled = True
    else:
        button.text = "Run"
        resetButton.disabled = False
        if not throwed:
            projangSlider.disabled = False
            prospbox.disabled = False
pauseButton = button(text="Run", bind=pause)

##重置按钮
def reset(button):
    global throwed,vball0,bgcube
    ###重置车和球的位置
    car.pos = vec(0,0,0)
    ball0.pos=car.pos - vec(5,-2.5,0)

    ###重置球的速度和状态
    vball0 = vcar+vproj
    throwed = False

    ###隐藏竖直轨迹条
    bgcube.visible = False

    ###重置向量和标签的位置
    VecVball0.pos = ball0.pos
    VecVball1.pos = ball0.pos
    VecVcar.pos = car.pos
    Vcartext.pos = VecVcar.pos+vec(0,3,0)

    ###重置按钮和滑条的状态
    pauseButton.disabled = False
    throwButton.disabled = False

    projangSlider.disabled = False
    prospbox.disabled = False
resetButton = button(text="Reset",bind=reset)

##发射按钮
def throw_the_ball(button):
    global throwed,bgcube
    throwed = True
    button.disabled = True

    bgcube.pos = ball0.pos+vec(0,5,0)
    bgcube.visible = True

throwButton = button(text="Throw!",bind=throw_the_ball)

##抛射角设置条
def setProjectionAngle():
    global vball0,vproj
    v = radians(projangSlider.value)
    vproj = vec(-20*cos(v),20*sin(v),0)
    vball0 = vproj + vcar

    VecVball1.axis = vec(-6*cos(v),6*sin(v),0)
    projangle.text = "\nCurrent:%d"%projangSlider.value
sc0.append_to_caption("\nProjection angle:")
projangSlider = slider(min=0,max=90,bind=setProjectionAngle,length=220,value=60)
projangle = wtext(text="\nCurrent:%d"%projangSlider.value)

##抛射速度设置框，及配套的提交按钮
def setProjectionSpeed():
    global inputcontent
    inputcontent = prospbox.number
sc0.append_to_caption("\n抛射速度：")
prospbox = winput(bind=setProjectionSpeed,text="20")


def submit():
    global inputcontent,vproj,vball0
    v = radians(projangSlider.value)
    vproj = vec(-inputcontent*cos(v),inputcontent*sin(v),0)
    vball0 = vproj + vcar
    projSpeedText.text = "\nCurrent:%.2fm/s"%inputcontent
submitButton = button(text="Submit",bind=submit)
projSpeedText = wtext(text="\nCurrent:20.00m/s")

def main():
     global running,vcar,dt,vball0,g,t,throwed
     if running:
        rate(50)#sleep(0.02)
        car.pos += vcar*dt
        VecVcar.pos += vcar*dt
        Vcartext.pos += vcar*dt
        if not throwed:
            ball0.pos += vcar*dt
            VecVball0.pos += vcar*dt
            VecVball1.pos += vcar*dt
        else:
            ball0.pos += vball0*dt 
            VecVball0.pos += vball0*dt
            VecVball1.pos += vball0*dt
            vball0 += g*dt
            t+=dt            
        if ball0.pos.y < -2:
            running = False
            resetButton.disabled = False
            pauseButton.disabled = True
            pauseButton.text = "Run"
if __name__ == "__main__":
    while True:
       main() 
 
