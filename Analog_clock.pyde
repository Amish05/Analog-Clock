def setup():
  size(260, 260)
  

  
def draw():
  fill(40)
  noStroke()
  ellipseMode(RADIUS)
  ellipse(130, 130, 125, 125)
  fill(255)
  ellipse(130, 130, 122, 122)
  texte()
  radius = min(height/1.7, width/1.7)
  cx = width/2
  cy = 260/2
  secondsRadius = radius * 0.72
  hoursTick = radius * 0.05
  minutesTick = hoursTick * 0.5
  for i in range(60):
      
     if (i%5==0):
         drawTickhour(cx, cy, i*6, secondsRadius, hoursTick)
     else:
         drawTick(cx, cy, i*6, secondsRadius, minutesTick)
  


  translate(130, 130)
  rotate(-HALF_PI)
  global hr,mn,sc
  hr = hour()
  mn = minute()
  sc = second()
  strokeWeight(2)
  stroke(255, 100, 150)
  noFill()
  secondAngle = map(sc, 0, 60, 0, TWO_PI)
  

  stroke(150, 100, 255)
  minuteAngle = map(mn, 0, 60, 0, TWO_PI)
  

  stroke(150, 255, 100)
  hourAngle = map(hr % 12, 0, 12, 0, TWO_PI)
  

  pushMatrix()
  rotate(secondAngle)
  stroke(0, 0, 0)
  line(0, 0, 105, 0)
  popMatrix()

  pushMatrix()
  rotate(minuteAngle)
  stroke(0,0, 0)
  line(0, 0, 85, 0)
  popMatrix()

  pushMatrix()
  rotate(hourAngle)
  stroke(0, 0, 0)
  line(0, 0, 60, 0)
  popMatrix()

  stroke(255)
  point(0, 0)
  
def texte():
    m=str(month())
    d=str(day())
    y=str(year())
    stroke(0)
    rect(130,205,70,15)
    textSize(12)
    fill(0)
    textAlign(CENTER)
    text(m+'.'+d+'.'+y,130,210)
    hr=hour()
    mn=minute()
    sc=second()
    text(str(hr)+':'+str(mn)+':'+str(sc),130,80)
def drawTick(x, y,  angle,len, weight):
    fill(0)
    noStroke()
    rectMode(CENTER)
    rect(x + cos(radians(angle-90))*len, y + sin(radians(angle-90))*len,weight, weight) 
def drawTickhour(x, y,  angle,len, weight):
    fill(angle*100, 0, 200, 156)
    noStroke()
    rectMode(CENTER)
    rect(x + cos(radians(angle-90))*len, y + sin(radians(angle-90))*len,weight, weight) 

  
