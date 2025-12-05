import serial
import time

# ตั้งค่าพอร์ตและ baudrate ตามที่ HuskyLens ใช้ (ปกติ 9600 หรือ 115200)
ser = serial.Serial('COM3', 9600, timeout=1)  # แก้ 'COM3' เป็นพอร์ตของคุณ
time.sleep(2)  # รอให้ serial พร้อม

print("เริ่มอ่านข้อมูลจาก HuskyLens...")

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8', errors='ignore').strip()
        if data:
            print("QR Output:", data)