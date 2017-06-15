#!/usr/bin/env python2.7
import time
import uinput
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

BOUNCETIME = 0.01

device = None
events = []

class Button:
	name = ""
	pinnumber = 0
	keycode = 0
	inverted = False

	last_state = False
	last_edge = time.time()

	def __init__(self, name, pinnumber, keycode, inverted = False):
		self.name = name
		self.pinnumber = pinnumber
		self.keycode = keycode
		self.inverted = inverted

		global events
		events.append(keycode);

		GPIO.setup(self.pinnumber, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
		GPIO.add_event_detect(self.pinnumber, GPIO.BOTH,  callback=self.callback)

	def callback(this, channel):
		global device

		now = time.time();
		if (now - this.last_edge) > BOUNCETIME:
			io = GPIO.input(this.pinnumber)
			if (this.inverted):
				io = not io

			if (io != this.last_state):
				if io:
					print "{:.3f}".format(now) + " | " + this.name.ljust(14) + " | " + str(this.keycode).ljust(9) + " | pressed"
					device.emit(this.keycode, 1)
				else:
					print "{:.3f}".format(now) + " | " + this.name.ljust(14) + " | " + str(this.keycode).ljust(9) + " | released"
					device.emit(this.keycode, 0)
				this.last_state = io
				this.last_edge = now

# Set up buttons by instanciating the class once for each giving a name
# and pin-assignment.
Button("JOYSTICK_UP",    22, uinput.KEY_UP)
Button("JOYSTICK_DOWN",  13, uinput.KEY_DOWN)
Button("JOYSTICK_LEFT",  26, uinput.KEY_LEFT, True) # Broken Microswitch does not close, but opens nicely.
Button("JOYSTICK_RIGHT",  6, uinput.KEY_RIGHT)

Button("START_1_PLAYER", 25, uinput.KEY_1)
Button("START_2_PLAYER", 18, uinput.KEY_2)

Button("BUTTON_RED",     23, uinput.KEY_LEFTCTRL)
Button("BUTTON_BLUE",    24, uinput.KEY_LEFTALT)
Button("BUTTON_YELLOW",  17, uinput.KEY_TAB)
Button("BUTTON_GREEN",   27, uinput.KEY_ENTER)
Button("BUTTON_PURPLE",   4, uinput.KEY_ESC)

Button("COIN",            5, uinput.KEY_5, True)

device = uinput.Device(events)

try:
	"""
	devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
	for device in devices:
		print(device.fn, device.name, device.phys)
	"""

	print "Processing GPIO-Pins for the MAMElet"
	print "Timestamp".ljust(14) + " | " + "Button".ljust(14) + " | " + "Key".ljust(9) +    " | " + "State".ljust(7) 	
	print "".ljust(14,"-") +      "-+-" + "".ljust(14,"-") +   "-+-" + "".ljust(9,"-") +   "-+-" + "".ljust(7,"-") 	

	# Nothing to do but stayin' alive
	while True:
		time.sleep(1)
		    
except KeyboardInterrupt:
	print "CTRL+C received"
	
print "Regular exit"
