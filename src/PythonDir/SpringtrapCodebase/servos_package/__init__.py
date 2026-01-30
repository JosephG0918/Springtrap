from adafruit_servokit import ServoKit
import logging
import time
from . import helpers

logging.basicConfig(
    filename="/home/oreo-pi/logs/servo_errors.log",  # Log file name
    level=logging.ERROR,                             # Only log errors and above
    filemode="w",
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Initialize the ServoKit for a 16-channel PWM driver (PCA9685); Pi HAT
kit = ServoKit(channels=16)

# Calibration runs first
helpers.calibration(kit)

# Servo channel assignments
L_EYE_BALL = 0
L_EYE_LID = 1
R_EYE_BALL = 2
R_EYE_LID = 3

JAW = 4

# Head movement servos
X_AXIS = 5
Y_AXIS_RIGHT = 6
Y_AXIS_LEFT = 7

# Single Servo Slow Movement
def slow_servo_move(servo_channel, target_angle, step_delay):
    """
    Smoothly moves a single servo to a target angle by stepping
    1 degree at a time.

    :param servo_channel: Servo channel number (0–15)
    :param target_angle: Desired servo angle (0–180 degrees)
    :param step_delay: Delay between steps (seconds)
                       Smaller = faster, Larger = smoother/slower
    """

    # Get the current servo angle
    # Current servo angle may be what the calibration.py script defines it as
    current_angle = kit.servo[servo_channel].angle

    # If there is no current servo angle, is None, then raise runtime error
    # Check logs
    if current_angle is None:
        logging.error(
            "Servo channel %d has no known angle. "
            "Calibration script may not have been run.",
            servo_channel
        )

        # Disable all servos for safety
        for i in range(16):
            kit.servo[i].angle = None

        raise RuntimeError("Servo angle is undefined — calibration required.")

    # Determine the direction of movement
    if target_angle > current_angle:
        step = 1
        angle_range = range(int(current_angle), int(target_angle) + 1, step)
    else:
        step = -1
        angle_range = range(int(current_angle), int(target_angle) - 1, step)

    # Incrementally move the servo
    for angle in angle_range:
        kit.servo[servo_channel].angle = angle
        time.sleep(step_delay)

    # Ensure it hits the exact final position
    kit.servo[servo_channel].angle = target_angle

# Dual Servo Synchronized Movement
def slow_servo_move_dual(ch1, target1, ch2, target2, step_delay):
    """
    Smoothly moves two servos at the same time, stepping them together
    so motion appears synchronized (useful for linkages like head tilt).

    :param ch1: First servo channel
    :param target1: Target angle for first servo
    :param ch2: Second servo channel
    :param target2: Target angle for second servo
    :param step_delay: Delay between steps (seconds)
    """

    current1 = kit.servo[ch1].angle
    current2 = kit.servo[ch2].angle

    if current1 is None or current2 is None:
        logging.error(
            "Dual servo move failed. Undefined angle(s): ch%d=%s, ch%d=%s. "
            "Calibration may not have been run.",
            ch1, current1, ch2, current2
        )

        # Disable all servos for safety
        for i in range(16):
            kit.servo[i].angle = None

        raise RuntimeError("One or more servo angles undefined")

    # Determine movement direction for each servo
    step1 = 1 if target1 > current1 else -1
    step2 = 1 if target2 > current2 else -1

    # Total steps needed (largest movement wins)
    max_steps = int(max(abs(target1 - current1), abs(target2 - current2)))

    # Move both servos step-by-step together
    for _ in range(max_steps):
        if current1 != target1:
            current1 += step1
            kit.servo[ch1].angle = current1

        if current2 != target2:
            current2 += step2
            kit.servo[ch2].angle = current2

        time.sleep(step_delay)

    # Force final exact positions
    kit.servo[ch1].angle = target1
    kit.servo[ch2].angle = target2

# neck x axis
def full_left_turn(step_delay=0.02):
    slow_servo_move(X_AXIS, 160, step_delay)

def half_left_turn(step_delay=0.02):
    slow_servo_move(X_AXIS, 135, step_delay)

def full_right_turn(step_delay=0.02):
    slow_servo_move(X_AXIS, 30, step_delay)

def half_right_turn(step_delay=0.02):
    slow_servo_move(X_AXIS, 45, step_delay)

def center_turn(step_delay=0.02):
    slow_servo_move(X_AXIS, 90, step_delay)

# neck y axis
def dance(rounds=1, step_delay=0.01):
    for _ in range(rounds):
        slow_servo_move_dual(Y_AXIS_RIGHT, 40, Y_AXIS_LEFT, 40, step_delay)
        slow_servo_move_dual(Y_AXIS_RIGHT, 140, Y_AXIS_LEFT, 140, step_delay)
    slow_servo_move_dual(Y_AXIS_RIGHT, 90, Y_AXIS_LEFT, 90, step_delay)

def chin_down(step_delay=0.01):
    slow_servo_move_dual(Y_AXIS_RIGHT, 140, Y_AXIS_LEFT, 40, step_delay)

def chin_up(step_delay=0.01):
    slow_servo_move_dual(Y_AXIS_RIGHT, 40, Y_AXIS_LEFT, 140, step_delay)

def chin_straight(step_delay=0.01):
    slow_servo_move_dual(Y_AXIS_RIGHT, 90, Y_AXIS_LEFT, 90, step_delay)

# jaw
def open_jaw(step_delay=0.02):
    slow_servo_move(JAW, 68, step_delay)

def close_jaw(step_delay=0.02):
    slow_servo_move(JAW, 108, step_delay)

def jaw_halfway_closed(step_delay=0.02):
    slow_servo_move(JAW, 88, step_delay)

# eyes
def eyes_straight(step_delay=0.01):
    slow_servo_move_dual(L_EYE_BALL, 90, R_EYE_BALL, 90, step_delay)

def eyes_left(step_delay=0.01):
    slow_servo_move_dual(L_EYE_BALL, 113, R_EYE_BALL, 113, step_delay)

def eyes_right(step_delay=0.01):
    slow_servo_move_dual(L_EYE_BALL, 66, R_EYE_BALL, 66, step_delay)

def eye_lids_normal(step_delay=0.01):
    slow_servo_move_dual(L_EYE_LID, 90, R_EYE_LID, 105, step_delay)

def eye_lids_wide(step_delay=0.01):
    slow_servo_move_dual(L_EYE_LID, 50, R_EYE_LID, 140, step_delay)

def eye_lids_lower(step_delay=0.01):
    slow_servo_move_dual(L_EYE_LID, 120, R_EYE_LID, 70, step_delay)
