# Search for BLE UART devices and list all that are found.
# Author: Tony DiCola
import atexit
import time
import sys

import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART

# add the ID of your arduino's bluetooth interface here
MYBLE = 'D0:E9:D8:E3:7E:12'


# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()


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

	# we are looking for this one
	# Found UART: Adafruit Bluefruit LE [4603dc3e-83cd-47e0-9cc6-49dbee415432]

	

	for device in new:
		print('Found UART: {0} [{1}]'.format(device.name, device.id))
		#print(device.id)
		if str(device.id) == MYBLE:
			print('Found it! Connecting...')
		#	device.connect()
			UART.discover(device)
			uart = UART(device)
			#command = input("Please enter commmand: ")	
			print('40')
			uart.write('40\r\n')
			time.sleep(2)
			print('150')
			uart.write('150\r\n')
			time.sleep(2)
			print('0')
			uart.write('3000\r\n')
			time.sleep(2)
			uart.write('djwhsyt\r\n')
			time.sleep(2)
			print('here')
			#break		
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
	device.disconnect()

finally:
	device.disconnect()
