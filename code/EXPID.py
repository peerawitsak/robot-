# PID Line Following Robot (Simulation-style)

import time

# PID constants
Kp = 0.6
Ki = 0.0
Kd = 0.2

# PID variables
previous_error = 0
integral = 0

# Base speed for motors
base_speed = 50

# Simulated sensor reading function (replace with actual sensor input)
def read_line_position():
    # Return error value: negative = left, positive = right, 0 = center
    # Example: -2 (far left), 0 (center), +2 (far right)
    return simulated_sensor_error()

def simulated_sensor_error():
    # Simulate error changing over time
    import random
    return random.randint(-3, 3)

# Motor control function (replace with actual motor driver code)
def set_motor_speed(left_speed, right_speed):
    print(f"Left Motor: {left_speed:.2f}, Right Motor: {right_speed:.2f}")

# Main loop
while True:
    error = read_line_position()
    integral += error
    derivative = error - previous_error

    # PID calculation
    PID_output = Kp * error + Ki * integral + Kd * derivative

    # Adjust motor speeds
    left_motor = base_speed - PID_output
    right_motor = base_speed + PID_output

    set_motor_speed(left_motor, right_motor)

    previous_error = error
    time.sleep(0.1)  # Delay for simulation