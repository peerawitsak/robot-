from math import pi
def cal_D ():
    rpm = int(input("rpm:"))#200
    rps = rpm/60 #หารอบต่อวินาที

    r = int(input("r:"))
    c = 2*pi*r # หาเส้นรอบวง


    t=1 #เวลา วินาที
    D = rps * c * t

    print(D)

def cal_V_from_dutycycle():
    dutycycle = int(input("dutycycle :"))
    rpm = int(input("rpm:"))
    Volt = int(input("V supply:"))
    r = int(input("r:"))
    Kv = rpm/Volt
    V = (dutycycle/100) * Volt *((2*pi*r)/60)
    print(V)

