from machine import Pin
import time

# กำหนดขา GPIO ที่ใช้ต่อกับ encoder
pin_a = Pin(14, Pin.IN, Pin.PULL_UP)  # ช่อง A
pin_b = Pin(15, Pin.IN, Pin.PULL_UP)  # ช่อง B

position = 0
last_state = pin_a.value()

def update_encoder(pin):
    global position, last_state
    current_state = pin_a.value()
    if current_state != last_state:
        if pin_b.value() != current_state:
            position += 1
        else:
            position -= 1
    last_state = current_state

# ตั้ง interrupt เมื่อมีการเปลี่ยนแปลงที่ช่อง A
pin_a.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=update_encoder)

# วนลูปแสดงค่าตำแหน่ง
while True:
    print("ตำแหน่ง:", position)
    time.sleep(0.1)
    
    
    
    
    #Firmata