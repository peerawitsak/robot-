import RPi.GPIO as GPIO
import pigpio as pig
import time 

#-------------------------- variable---------------------------------
motor_position = 0

Vmax = 80 #ความเร็วมากสุดที่ใช้ได้ คิดจาก dutycycle รอบ 
k = 2 #ไว้จูนความเร็วของสมาการ



#---------------------------- pinout ----------------------------------
motor_up = 111
motor_down = 111

PWM_A =111
PWM_B = 111

position_A = 17
position_B = 27 


#----------------------------set up -------------------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(motor_up,GPIO.OUT)
GPIO.setup(motor_down,GPIO.OUT)

GPIO.setup(PWM_A,GPIO.OUT)
GPIO.setup(PWM_B,GPIO.OUT)

PWMA =GPIO.PWM(PWM_A,1000)
PWMB =GPIO.PWM(PWM_B,1000)

PWMA.start(0)
PWMB.start(0)  

GPIO.setup(position_A,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(position_B,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#-------------------------------------function---------------------------------
def Motor_read():
    global motor_position
    if GPIO.input(position_A) == GPIO.input(position_B):
        motor_position += 1   # หมุนไปทางหนึ่ง
    else:
        motor_position -= 1   # หมุนไปอีกทางหนึ่ง
    #print("Position:", motor_position)


def Velocity(d): #d = ระยะห่าง ,ใช้สมาการ Exponential ยิ่งห่างมากยิ่งเร็ว ยิ่งห่างน้อยยิ่งช้า
    ans = Vmax *(1-(2.72**((-k)*d)))#2.72 = e
    return ans



#---------------------------main -------------------------------------

GPIO.add_event_detect(position_A, GPIO.BOTH, callback=Motor_read())# ผูก interrupt กับขา position_A











#--------------------------------Loop---------------------------------------
while True :
        print(motor_position)
