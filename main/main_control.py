from constan import *
from function import *

#----------------------------setup-------------------------------------#

GPIO.setmode(GPIO.BCM)#mode of set pin 
#GPIO.setmode(GPIO.Board)

#set sensor
GPIO.setup(sen1,GPIO.IN)
GPIO.setup(sen2,GPIO.IN)
GPIO.setup(sen3,GPIO.IN)
GPIO.setup(sen4,GPIO.IN)
GPIO.setup(sen5,GPIO.IN)
GPIO.setup(sen6,GPIO.IN)
GPIO.setup(sen7,GPIO.IN)
GPIO.setup(sen8,GPIO.IN)

GPIO.setup(sen9,GPIO.IN)
GPIO.setup(sen10,GPIO.IN)

GPIO.setup(button,GPIO.IN)

GPIO.setwarnings(False)

GPIO.setup(front_right,GPIO.OUT)
GPIO.setup(front_left,GPIO.OUT)
GPIO.setup(back_right,GPIO.OUT)
GPIO.setup(back_left,GPIO.OUT)

GPIO.setup(pwm_a,GPIO.OUT)
GPIO.setup(pwm_b,GPIO.OUT)

pwm_a = GPIO.PWM(pwm_a,1000) # forward (pin,frequency)
pwm_b = GPIO.PWM(pwm_b,1000) # backward (pin,frequency)

pwm_a.start(0) #start with 0% dutycycle
pwm_b.start(0) #start with 0% dutycycle

#--------------------------main ---------------------------------#ทำงานรอบเดียว
#className "robot"
rb = Robot(Kp,Ki,Kd,Speed,Target)#เคยสร้างแล้วที่ function.py เพราะต้องสร้างฟังชั่น
# robot.update() # update ค่า .position-->._error-->.pid_value-->speed motor , อ่านเส้นดำ .black_line
# robot.Track_forward()
# robot.Track_backward()

#-------------------------- Loop ----------------------------------
while True():
    
    pass
# motor_contro(PID_cal((ReadSensor()-target)))
