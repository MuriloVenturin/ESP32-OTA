from machine import Pin
from time import sleep
from ota_updater import OTAUpdater


o = OTAUpdater('https://github.com/MuriloVenturin/ESP32-OTA', main_dir = 'main')

def download_and_install_update_if_available():
	global o
	o.download_and_install_update_if_available('NET_2GF0E80D', '69F0E80D')
  
def start():
	global o
	led = Pin(2, Pin.OUT)

	while True:  
		led.value(not led.value())
		sleep(0.5)

def boot():
	global o
	
	o.using_network('NET_2GF0E80D', '69F0E80D')
	o.check_for_update_to_install_during_next_reboot()
	download_and_install_update_if_available()
	start()
	boot()

boot()

