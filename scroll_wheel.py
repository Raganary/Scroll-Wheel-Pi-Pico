#program used to make rotary encoder act as a scroll wheel
import time
import digitalio
import board
import rotaryio
import usb_hid

from adafruit_hid.mouse import Mouse

# Rotary encoder connections to board
encoder = rotaryio.IncrementalEncoder(board.GP4, board.GP3)
encoderSw = digitalio.DigitalInOut(board.GP2)
encoderSw.direction = digitalio.Direction.INPUT
encoderSw.pull = digitalio.Pull.UP
lastPosition = 0

# LED flashes when a movement is made
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

# USB device
m = Mouse(usb_hid.devices)

# button delay
delay = 0.2

# loop
while True:
    # poll encoder position
    position = encoder.position
    if position != lastPosition:
        led.value = True
        if lastPosition < position:
            m.move(0,0,-1)
        else:
            m.move(0,0,1)
        lastPosition = position
        led.value = False
    
    # poll encoder button
    if encoderSw.value == 0:
        m.click(Mouse.LEFT_BUTTON)
        led.value = True
        time.sleep(delay)
        led.value = False
        
    time.sleep(0.1)