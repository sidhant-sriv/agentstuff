import serial
import time
from llama_index.core.tools import FunctionTool
from typing import List

PORT = "/dev/cu.usbserial-210"
BAUDRATE = 115200  # Updated to match Arduino code

# Global serial connection for persistent communication
_serial_connection = None

def _get_serial_connection():
    """
    Gets or creates a persistent serial connection.
    """
    global _serial_connection
    if _serial_connection is None or not _serial_connection.is_open:
        _serial_connection = serial.Serial(PORT, BAUDRATE, timeout=2)
        time.sleep(2)  # Wait for ESP32 to stabilize
        # Clear any startup messages
        while _serial_connection.in_waiting > 0:
            _serial_connection.readline()
    return _serial_connection

def _send_command(command: str) -> str:
    """
    Sends a command to the Arduino and returns the response.
    
    Args:
        command (str): The command to send (e.g., "servo:angle:90")
    
    Returns:
        str: The response from the Arduino
    """
    try:
        ser = _get_serial_connection()
        ser.write(f"{command}\n".encode())
        time.sleep(0.2)  # Give Arduino time to process
        
        response = ""
        while ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            if line:
                response += line + "\n"
        
        return response.strip() if response else "No response received"
    except serial.SerialException as e:
        return f"Error: {e}"

def control_servo_angle(angle: int) -> str:
    """
    Controls the servo motor by setting its angle.
    
    Args:
        angle (int): The angle to set the servo to (0-180 degrees).
    
    Returns:
        str: The response from the Arduino indicating success or error.
    
    Example:
        - If user says "move servo to 90 degrees", use angle=90
        - If user says "turn servo left", use angle=0
        - If user says "turn servo right", use angle=180
        - If user says "center the servo", use angle=90
    """
    if angle < 0 or angle > 180:
        return f"Error: Angle must be between 0 and 180. Got: {angle}"
    
    command = f"servo:angle:{angle}"
    return _send_command(command)

def control_servo_microseconds(microseconds: int) -> str:
    """
    Controls the servo motor by setting its pulse width in microseconds.
    
    Args:
        microseconds (int): The pulse width in microseconds (500-2500).
    
    Returns:
        str: The response from the Arduino indicating success or error.
    
    Example:
        - For fine-grained control, use microseconds between 500 and 2500
        - 1500 microseconds is typically the center position
    """
    if microseconds < 500 or microseconds > 2500:
        return f"Error: Microseconds must be between 500 and 2500. Got: {microseconds}"
    
    command = f"servo:us:{microseconds}"
    return _send_command(command)

def control_led(state: str) -> str:
    """
    Controls the LED by turning it on or off.
    
    Args:
        state (str): The desired state of the LED ("on" or "off").
    
    Returns:
        str: The response from the Arduino indicating success or error.
    
    Example:
        - If user says "turn on the LED" or "light on", use state="on"
        - If user says "turn off the LED" or "light off", use state="off"
        - If user says "blink", you need to call this function multiple times with delays
    """
    state = state.lower()
    if state not in ["on", "off"]:
        return f"Error: State must be 'on' or 'off'. Got: {state}"
    
    command = f"led:{state}"
    return _send_command(command)

def get_distance() -> str:
    """
    Reads the distance from the HC-SR04 ultrasonic sensor.
    
    Returns:
        str: The distance measured in centimeters, or an error message.
    
    Example:
        - If user asks "how far is the object?", call this function
        - If user asks "measure distance", call this function
        - If user asks "is something nearby?", call this function
    """
    command = "distance:get"
    return _send_command(command)

def is_serial_hardware_available() -> bool:
    """
    Checks if the serial hardware device is available.
    
    Returns:
        bool: True if the serial hardware device can be opened, False otherwise.
    """
    try:
        _get_serial_connection()
        return True
    except serial.SerialException:
        return False

def close_serial_connection():
    """
    Closes the serial connection if it's open.
    """
    global _serial_connection
    if _serial_connection and _serial_connection.is_open:
        _serial_connection.close()
        _serial_connection = None

def serial_hardware_operations() -> list:
    """
    Returns a list of available serial hardware functions.
    """
    return [
        control_servo_angle,
        control_servo_microseconds,
        control_led,
        get_distance,
        is_serial_hardware_available
    ]

def return_serial_hardware_operations() -> list:
    """
    Returns the serial hardware functions as FunctionTool objects.
    """
    return [FunctionTool.from_defaults(fn=func) for func in serial_hardware_operations()]


