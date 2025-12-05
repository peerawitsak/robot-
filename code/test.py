
def Forward_Until_Black(i):#เดินหน้าจนกว่าจะเจอเส้นดำ 1;ทั้งเส้น 2;ดำขวา 3;ดำซ้าย 
    while CheckBlackLine>i: # หยุดตอนเจอ เส้นดำ 1ครั้ง
        forward()
    time.sleep(Time_delay)
    #delay ให้ เกินเส้นดำ
    
def Start_TO_Box():#วิ่งจากstartไปเก็บกล่อง
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 

def Box_To_Left():#วิ่งหลังจากเก็บกล่องแล้วไปทางซ้าย
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    TurnLeft()
    Forward_Until_Black(2)#เจอเส้นดำขวา
    TurnRight()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 

def Box_To_Right():#วิ่งหลังจากเก็บกล่องแล้วไปทางขวา
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    TurnRight()
    Forward_Until_Black(3) #เจอเส้นดำซ้าย
    TurnLeft()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 

def Box_To_Mid():#วิ่งหลังจากเก็บกล่องแล้วตรงไปขึ้นสะพาน
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    #สำหรับขึ้นสะพาน
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    
def Left_TO_Right():#วิ่งจากซ้ายหลังวางกล่องแล้วไปขวา
    UTurn()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(3)#เจอเส้นซ้าย
    TurnLeft()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(3)#เจอเส้นซ้าย
    TurnLeft()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 

def Right_TO_Left():#วิ่งจากขวาหลังวางกล่องแล้วไปซ้าย
    UTurn()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(2)#เจอเส้นซ้าย
    TurnRight()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(2)#เจอเส้นซ้าย
    TurnRight()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 

def Left_To_Start():#วิ่งจากซ้ายกลับไปจุดstart
    UTurn()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(3)#เจอเส้นซ้าย
    TurnLeft()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    TurnRight()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น

def Right_To_Start():#วิ่งจากขวากลับไปจุดstart
    UTurn()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 
    Forward_Until_Black(2)#เจอเส้นซ้าย
    TurnRight()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น
    TurnLeft()
    Forward_Until_Black(1)#เจอเส้นดำทั้งเส้น 

