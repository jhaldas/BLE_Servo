# Searches for BLE UART devices and connect to device id MYBLE.
# Prompts user for inpet to move servo to specified position.
# Author: Jonny Haldas
# Connection code taken from: Tony DiCola's list_uarts.py
import atexit
import time
import sys

import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART

# add the ID of your arduino's bluetooth interface here
MYBLE = 'D0:E9:D8:E3:7E:12'


# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()


# Call this method to use user input to move servo to given position
def moveServo(servo):
	bool = True
	while bool ==  True:
		try:
			move = int(raw_input('Input between 0-180 degrees, or -1 to stop): '))
			if move == -1:
				bool = False
			elif move <= 180 or move >= 0:
				move = str(move)
				servo.write(move + '\r\n')
		except ValueError:
			print("Invalid Input")
	print("Completed.")

# Main function implements the program logic so it can run in a background
# thread.  Most platforms require the main thread to handle GUI events and other
# asyncronous events like BLE actions.  All of the threading logic is taken care
# of automatically though and you just need to provide a main function that uses
# the BLE provider.
def main():

    # Clear any cached data because both bluez and CoreBluetooth have issues with
    # caching data and it going stale.
    ble.clear_cached_data()

    # Get the first available BLE network adapter and make sure it's powered on.
    adapter = ble.get_default_adapter()
    adapter.power_on()
    print('Using adapter: {0}'.format(adapter.name))

    # Start scanning with the bluetooth adapter.
    adapter.start_scan()

    # Use atexit.register to call the adapter stop_scan function before quiting.
    # This is good practice for calling cleanup code in this main function as
    # a try/finally block might not be called since this is a background thread.
    atexit.register(adapter.stop_scan)
    print('Searching for all UART devices...')

    print('Press Ctrl-C to quit (will take ~30 seconds on OSX).')
    # Enter a loop and print out whenever a new UART device is found.
    known_uarts = set()

    print('Searching for device with ID: ' + MYBLE)
    while True:
        # Call UART.find_devices to get a list of any UART devices that
        # have been found.  This call will quickly return results and does
        # not wait for devices to appear.
        found = set(UART.find_devices())

        # Check for new devices that haven't been seen yet and print out
        # their name and ID (MAC address on Linux, GUID on OSX).
        new = found - known_uarts

	for device in new:
		print('Found UART: {0} [{1}]'.format(device.name, device.id))
		#print(device.id)
		if str(device.id) == MYBLE:
			print('Found it! Connecting...')
			#device.connect() 	#Needed for Mac but not Linux
			UART.discover(device)
			uart = UART(device)
			moveServo(uart)
			sys.exit()
		else:
			 print('Not Yet')
        known_uarts.update(new)
        # Sleep for a second and see if new devices have appeared.
        time.sleep(1.0)


try:
	# Initialize the BLE system.  MUST be called before other BLE calls!
	ble.initialize()

	# Start the mainloop to process BLE events, and run the provided function in
	# a background thread.  When the provided main function stops running, returns
	# an integer status code, or throws an error the program will exit.
	ble.run_mainloop_with(main)
except KeyboardInterrupt:
	sys.exit(0)
	#device.disconnect()

finally:
	#device.disconnect()
	sys.exit()
