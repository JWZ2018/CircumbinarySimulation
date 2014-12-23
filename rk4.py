from pygame import *
from math import *

size=length,width=(1024,768)#dimensions of screen
screen=display.set_mode(size)
init()
running=True
ti=0
R=10
G=100
M=1
mRatio=2
#Turning Ellipse
##px=100
##py=0
#L1
##px=R*0.712256
##py=0
#L2
##px=R*3.74714
##py=0
#L3
##px=R*(-1*3.409084)
##py=0
#L4
##px=R*(mRatio-1)/2.0 + 1
##py=R*(mRatio+1)/2.0*3**0.5*(-1)
#L5
##px=R*(mRatio-1)/2.0 + 1
##py=R*(mRatio+1)/2.0*3**0.5
#Random
px=R*2.37
py=R*4.23
angle=atan((mRatio-1)/float(mRatio+1)/3**0.5)
##vx=(G*M*hypot(px,py)**2/((mRatio+1)**2*R**3))**0.5*cos(angle)
##vy=(G*M*hypot(px,py)**2/((mRatio+1)**2*R**3))**0.5*sin(angle)
##vy=(G*M*(mRatio+1)/px)**0.5
##vx=0
vy=(G*M*px**2/(9*R**3))**0.5
vx=0
dt=0.001
om=(G*M)**0.5/((mRatio+1)*R**1.5)
count=0
totalTime=100000
scale=2
r1x=mRatio*R*cos(om*ti)
r1y=mRatio*R*sin(om*ti)
r2x=-1*R*cos(om*ti)
r2y=-1*R*sin(om*ti)
paused=False
def g(t,rx,ry):
    return -rx,-ry
def f(t,rx,ry):
    global r1x, r1y, r2x, r2y
    r1x=mRatio*R*cos(om*t)
    r1y=mRatio*R*sin(om*t)
    r2x=-1*R*cos(om*t)
    r2y=-1*R*sin(om*t)
    term1x=float(G*M)/((rx-r1x)**2+(ry-r1y)**2)**1.5*(r1x-rx)
    term1y=float(G*M)/((rx-r1x)**2+(ry-r1y)**2)**1.5*(r1y-ry)
    term2x=mRatio*float(G*M)/((rx-r2x)**2+(ry-r2y)**2)**1.5*(r2x-rx)
    term2y=mRatio*float(G*M)/((rx-r2x)**2+(ry-r2y)**2)**1.5*(r2y-ry)
    
    return term1x+term2x,term1y+term2y
draw.circle(screen,(0,0,255),(int(512+scale*px),int(384+scale*py)),4)
draw.circle(screen,(0,0,255),(int(512+scale*r1x),int(384+scale*r1y)),2)
draw.circle(screen,(0,0,255),(int(512+scale*r2x),int(384+scale*r2y)),4)
while running:
    for evt in event.get():
        if evt.type==QUIT or key.get_pressed()[27]==1:
            running=False
        if key.get_pressed()[112]==1:
            paused= not paused
    if not paused:
        krx1=vx
        kry1=vy
        ans1=f(ti,px,py)
        kvx1=ans1[0]
        kvy1=ans1[1]

        krx2=vx+0.5*krx1*dt
        kry2=vy+0.5*kry1*dt
        ans2=f(ti+dt/2,px+0.5*krx1*dt,py+0.5*kry1*dt)
        kvx2=ans2[0]
        kvy2=ans2[1]

        krx3=vx+0.5*krx2*dt
        kry3=vy+0.5*kry2*dt
        ans3=f(ti+dt/2,px+0.5*krx2*dt,py+0.5*kry2*dt)
        kvx3=ans3[0]
        kvy3=ans3[1]

        krx4=vx+krx3*dt
        kry4=vy+kry3*dt
        ans4=f(ti+dt,px+krx3*dt,py+kry3*dt)
        kvx4=ans4[0]
        kvy4=ans4[1]

        px+=(dt/6.0)*(krx1+2*krx2+2*krx3+krx4)
        py+=(dt/6.0)*(kry1+2*kry2+2*kry3+kry4)
        vx+=(dt/6.0)*(kvx1+2*kvx2+2*kvx3+kvx4)
        vy+=(dt/6.0)*(kvy1+2*kvy2+2*kvy3+kvy4)

        ti+=dt
        count+=1
        if count%100==0:
            #screen.fill((0,0,0))
            draw.line(screen,(255,255,255),(0,384),(1024,384))
            draw.line(screen,(255,255,255),(512,0),(512,768))
            draw.circle(screen,(0,255,0),(int(512+scale*r1x),int(384+scale*r1y)),0)
            draw.circle(screen,(0,255,0),(int(512+scale*r2x),int(384+scale*r2y)),0)
            draw.circle(screen,(255,0,0),(int(512+scale*px),int(384+scale*py)),0)
            display.flip()
##            draw.circle(screen,(0,0,0),(int(512+scale*r1x),int(384+scale*r1y)),5)
##            draw.circle(screen,(0,0,0),(int(512+scale*r2x),int(384+scale*r2y)),10)
quit()
