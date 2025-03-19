import gpiod
import time

# Define the GPIO chip and line (pin) to use
CHIP = 'gpiochip0'  # Use the AO GPIO chip
SERVO_PIN = 6       # GPIOAO_6 maps to Linux GPIO number 6 on gpiochip0

# Set up the GPIO chip and line
chip = gpiod.Chip(CHIP)
line = chip.get_line(SERVO_PIN)

# Request the line for output
line.request(consumer="servo", type=gpiod.LINE_REQ_DIR_OUT)

# Pulse width range (in seconds)
PULSE_MIN = 0.000500  # 500 µs (0 degrees)
PULSE_MAX = 0.002500  # 2500 µs (180 degrees)
PULSE_CENTER = 0.001500  # 1500 µs (90 degrees)

# Function to set servo angle
def set_servo_angle(angle):
    # Map angle (0 to 180) to pulse width (PULSE_MIN to PULSE_MAX)
    pulse_width = PULSE_MIN + (angle / 180.0) * (PULSE_MAX - PULSE_MIN)
    line.set_value(1)
    time.sleep(pulse_width)  # Set pulse width
    line.set_value(0)
    time.sleep(0.020 - pulse_width)  # Complete the 20 ms cycle

try:
    # Start at 0 degrees
    set_servo_angle(0)  # 0 degrees
    time.sleep(1)       # Wait 1 second

    # Rotate to 45 degrees
    set_servo_angle(45)  # 45 degrees
    time.sleep(1)        # Wait 1 second

finally:
    # Clean up the GPIO line
    line.release()
