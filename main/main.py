from machine import Pin
from time import sleep
from ota_updater import OTAUpdater

def download_and_install_update_if_available():
  o = OTAUpdater('https://github.com/MuriloVenturin/ESP32-OTA')
  o.download_and_install_update_if_available('RunPal-GUEST', 'runpalbr')

def start():
  led = Pin(2, Pin.OUT)
  while True:
    led.value(not led.value())
    sleep(0.5)

def boot():
  download_and_install_update_if_available()
  start()
  boot()


if __name__ == '__main__':
	
	boot()

