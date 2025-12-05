"""
code นี้ใช้สำหรับ rasbery pi 
ยังไม่ทดลองเขียนจาก การจิตนาการล้วนๆ แก้ล่าสุดวันที่ 12//2025 format mm/dd/YYYY

ยังไม่ ปรับค่า 
ใช้ sensor สะท้อนแสง analog 
pinout ยังกำหนดไม่ครบ

"""
import RPi.GPIO as GPIO
import pigpio as pig
import time 

#--------------------------variable---------------------------------
#รูปแบบ
patterns = {
    (0,1,1,1,1,1,1,1):1,
    (0,0,1,1,1,1,1,1):2,
    (1,0,1,1,1,1,1,1):3,
    (1,0,0,1,1,1,1,1):4,
    (1,1,0,1,1,1,1,1):5,
    (1,1,0,0,1,1,1,1):6,
    (1,1,1,0,1,1,1,1):7,
    (1,1,1,0,0,1,1,1):8,
    (1,1,1,1,0,1,1,1):9,
    (1,1,1,1,0,0,1,1):10,
    (1,1,1,1,1,0,1,1):11,
    (1,1,1,1,1,0,0,1):12,
    (1,1,1,1,1,1,0,1):13,
    (1,1,1,1,1,1,0,0):14,
    (1,1,1,1,1,1,1,0):15,
}

patterns_black_line = {
    (0,0,0,0,0,0,0,0):1,
    (1,1,1,0,0,0,0,0):2,
    (0,0,0,0,0,1,1,1):3,
    (1,1,1,0,0,1,1,1):4
}

# senser avg
# avgBlack = 200
# avgGreen = 600
# avgWhite = 900
# avgBlue = 300

#delay
TimeOfRun =0.050#เวลาให้ motor ทำงานสำหรับวิ่งปกติ milisec หมายเหตุยังไม่ใช้ในวันที่ 11/27/2025
TimeOfTurn = 0.050#เวลา ให้ motorทำงานสำหรับการเลี้ยว  milisec
Time_delay = 0.020#delay ให้ เกินเส้นดำ milisec

# speed motor
Speed = 30 # dutycycle 50% 

TurnSpeed = 50
BackSpeed = 20

# PID constants 
Kp = 5
Ki = 0
Kd = 0

# PID variable
target = 8

Integral_x = 0 #x หมายถึง error
previous_x = 0 #x หมายถึง error

previous_T = 0 # เก็บเวลา us


pid_value = 0
P = 0
I = 0
D = 0

#error = Realposition - target 
error = 0

#-------------------------------------set pinout------------------------------
#set sensor pin 
sen1 = 17 # pin 11
sen2 = 27 # pin 13
sen3 = 22 # pin 13
sen4 = 23 # pin 15
sen5 = 24 # pin 29
sen6 = 25 
sen7 = 5
sen8 = 6

#ปุ่ม
button = 4

#I2C for LCD
sda = 2 #pin 3  ยังไม่กำหนด IO
scl = 3 #pin 5 ยังไม่กำหนด IO

#set motor

PWM_B = 21 #40
front_right = 12 #32
back_right = 16 #36

PWM_A = 20 #38
front_left = 19 #35
back_left  = 26 #37

#----------------------------setup-------------------------------------#

GPIO.setmode(GPIO.BCM)#mode of set pin 
#GPIO.setmode(GPIO.Board)

#set sensor
GPIO.setup(sen1,GPIO.IN)
GPIO.setup(sen2,GPIO.IN)
GPIO.setup(sen3,GPIO.IN)
GPIO.setup(sen4,GPIO.IN)
GPIO.setup(sen5,GPIO.IN)

GPIO.setup(button,GPIO.IN)

GPIO.setwarnings(False)

GPIO.setup(front_right,GPIO.OUT)
GPIO.setup(front_left,GPIO.OUT)
GPIO.setup(back_right,GPIO.OUT)
GPIO.setup(back_left,GPIO.OUT)

GPIO.setup(PWM_A,GPIO.OUT)
GPIO.setup(PWM_B,GPIO.OUT)

PWMA = GPIO.PWM(PWM_A,1000) # forward (pin,frequency)
PWMB = GPIO.PWM(PWM_B,1000) # backward (pin,frequency)

PWMA.start(0) #start with 0% dutycycle
PWMB.start(0) #start with 0% dutycycle


#----------------------------------function ----------------------------------------

############################# การคำนวณ ###############################

# def Ana2Digi(senser): # แยกขาวดำ output 1 or 0
#     value = GPIO.input(senser)
#     if(value<=avgBlack):
#         return 0 
#     elif(value>avgBlack):
#         return 1
#     else :
#         pass

def CheckBlackLine():#อ่านค่อ และ เช็คเส้นดำ out 1:เส้นดำทั้งเส้น 2:เส้นดำขวา 3:เส้นดำซ้าย and 0 ถ้าไม่เจอ 
    SenVal = [0,0,0,0,0,0,0,0]
    SenVal[0]=GPIO.input(sen1)
    SenVal[1]=GPIO.input(sen2)
    SenVal[2]=GPIO.input(sen3)
    SenVal[3]=GPIO.input(sen4)
    SenVal[4]=GPIO.input(sen5)
    SenVal[5]=GPIO.input(sen6)
    SenVal[6]=GPIO.input(sen7)
    SenVal[7]=GPIO.input(sen8)
    
    return patterns_black_line.get(tuple(SenVal),0)

def ReadSensor():#อ่านค่า ส่งค่อออกเป็นposition 1 - 15 and 0 ถ้าไ่ม่เจอ
    SenVal = [0,0,0,0,0,0,0,0]
    SenVal[0]=GPIO.input(sen1)
    SenVal[1]=GPIO.input(sen2)
    SenVal[2]=GPIO.input(sen3)
    SenVal[3]=GPIO.input(sen4)
    SenVal[4]=GPIO.input(sen5)
    SenVal[5]=GPIO.input(sen6)
    SenVal[6]=GPIO.input(sen7)
    SenVal[7]=GPIO.input(sen8)
    
    return patterns.get(tuple(SenVal),0)

def PID_cal(x):# x = error ; error = position - target
    global previous_T, Integral_x, previous_x

    current_T = pig.pi().get_current_tick()
    delta_T  =(current_T-previous_T)/ 1.0e6
    previous_T = current_T

    P = x
    I = Integral_x + (x*delta_T)
    D = (x-previous_x)/delta_T if delta_T > 0 else 0 # จริง if condition else ไม่จริง // กัน หารด้วย 0


    pid_value = (Kp*P)+(Ki*I)+(Kd*D)
    
    Integral_x = I
    previous_x = x
    return pid_value

def motor_contro(pid):#ทำการปรับจูนค่าความเร็ว motor ซ้ายขวา 
    right_speed_motor = Speed + pid
    left_speed_motor = Speed - pid
    
    if(right_speed_motor>100):
        right_speed_motor = 100
    elif(right_speed_motor<-100):
        right_speed_motor=-100
    
    if(left_speed_motor>100):
        left_speed_motor = 100
    elif(left_speed_motor<-100):
        left_speed_motor =-100
    
    return left_speed_motor,right_speed_motor  

# PID_error = PID_cal(ReadSensor())11

# sp_left , sp_rigth = motor_contro(PID_error) 

# forward(sp_left,sp_rigth)

######################## การทำงานพื้นฐาน ######################

def motor_dive(speedleft,speedright):#motor drive ราค่าความเร็วซ้ายขวา 
    
    if(speedright>0 and speedleft>0):
        PWMA.ChangeDutyCycle(speedleft)
        PWMB.ChangeDutyCycle(speedright)
        GPIO.output(front_right,1) 
        GPIO.output(front_left,1)
        GPIO.output(back_right,0)
        GPIO.output(back_left,0)
    elif(speedright<0 and speedleft>0):
        PWMA.ChangeDutyCycle(speedleft)
        PWMB.ChangeDutyCycle(-speedright)
        GPIO.output(front_right,0) 
        GPIO.output(front_left,1)
        GPIO.output(back_right,1)
        GPIO.output(back_left,0)
    elif(speedright>0 and speedleft<0):
        PWMA.ChangeDutyCycle(-speedleft)
        PWMB.ChangeDutyCycle(speedright)
        GPIO.output(front_right,1)
        GPIO.output(front_left,0)
        GPIO.output(back_right,0)
        GPIO.output(back_left,1)
    elif(speedright<0 and speedleft<0):
        PWMA.ChangeDutyCycle(-speedleft)
        PWMB.ChangeDutyCycle(-speedright)
        GPIO.output(front_right,0) 
        GPIO.output(front_left,0)
        GPIO.output(back_right,1)
        GPIO.output(back_left,1)
    elif(speedleft == 0 and speedright == 0):
        PWMA.ChangeDutyCycle(0)
        PWMB.ChangeDutyCycle(0)
        GPIO.output(front_right,0) 
        GPIO.output(front_left,0)
        GPIO.output(back_right,0)
        GPIO.output(back_left,0)
    else: 
        pass
    
def motor_stop():#หยุดการทำงาน motor
    PWMA.ChangeDutyCycle(0)
    PWMB.ChangeDutyCycle(0)
    GPIO.output(front_right,0) 
    GPIO.output(front_left,0)
    GPIO.output(back_right,0)
    GPIO.output(back_left,0)

def forward(speedleft,speedright):#เดินไปข้างหน้าด้วยการ tag แบบ pid 
    # คำนวนการดึงตัวกลับ เอาไปขับ motor
    motor_dive(speedleft,speedright)
    #time.sleep(TimeOfRun)
    
def TurnRight():#เลี้ยวขวา ด้วยความเร็วตาม Turnspeed ทำงานนาน TimeOfTurn
    # motor_dive(TurnSpeed,-TurnSpeed)
    PWMA.ChangeDutyCycle(speedleft)
    GPIO.output(front_right,0) 
    GPIO.output(front_left,1)
    PWMB.ChangeDutyCycle(-speedright)
    GPIO.output(back_right,1)
    GPIO.output(back_left,0)
    time.sleep(TimeOfTurn)
    motor_stop()

def TurnLeft(speed):#เลี้ยวซ้าย ด้วยความเร็วตาม Turnspeed ทำงานนาน TimeOfTurn
    motor_dive(-speed,speed)
    time.sleep(TimeOfTurn)
    motor_stop()

def UTurn(speed):#เลี้ยวขวายาวจนกลับหัว
    motor_dive(speed,-speed)
    time.sleep(TimeOfTurn*2)
    motor_stop()

######################## การเดินหลัก ######################

#--------------------------main ---------------------------------#




#-------------------------- Loop ----------------------------------
motor_contro(PID_cal((ReadSensor()-target)))



