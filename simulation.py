from pygame import *
from math import *
size=length,width=(1024,768)#dimensions of screen
screen=display.set_mode(size)
init()
running=True
t=0
R=10
G=100
M=1
rx=80
ry=0
vx=0
vy=(3*G*M/(rx))**0.5
dt=0.01
om=(G*M)**0.5/(3*R**1.5)
r1x=2*R*cos(om*t)
r1y=2*R*sin(om*t)
r2x=-1*R*cos(om*t)
r2y=-1*R*sin(om*t)
count=0
totalTime=100000
scale=2
while running:
    for evt in event.get():
        if evt.type==QUIT or key.get_pressed()[27]==1:
            running=False
    term1x=float(G*M)/((rx-r1x)**2+(ry-r1y)**2)**1.5*(r1x-rx)
    term1y=float(G*M)/((rx-r1x)**2+(ry-r1y)**2)**1.5*(r1y-ry)
    term2x=2*float(G*M)/((rx-r2x)**2+(ry-r2y)**2)**1.5*(r2x-rx)
    term2y=2*float(G*M)/((rx-r2x)**2+(ry-r2y)**2)**1.5*(r2y-ry)
    ax=term1x+term2x
    ay=term1y+term2y
    vx+=ax*dt
    vy+=ay*dt
    rx+=vx*dt
    ry+=vy*dt
    t+=dt
    r1x=2*R*cos(om*t)
    r1y=2*R*sin(om*t)
    r2x=-1*R*cos(om*t)
    r2y=-1*R*sin(om*t)
    count+=1
    if count>totalTime:
        running=False
    draw.line(screen,(255,255,255),(0,384),(1024,384))
    draw.line(screen,(255,255,255),(512,0),(512,768))
    draw.circle(screen,(0,255,0),(int(512+scale*r1x),int(384+scale*r1y)),5)
    draw.circle(screen,(0,255,0),(int(512+scale*r2x),int(384+scale*r2y)),10)
    draw.circle(screen,(255,0,0),(int(512+scale*rx),int(384+scale*ry)),2)
    display.flip()
time.wait(1000)
quit()
