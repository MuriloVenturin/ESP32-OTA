from machine import Pin
from time import sleep
from ota_update.main.ota_updater import OTAUpdater

def download_and_install_update_if_available():
  o = OTAUpdater('url-to-your-github-project')
  o.download_and_install_update_if_available('wifi-ssid', 'wifi-password')

def start():
  led = Pin(2, Pin.OUT)
  while True:
    led.value(1)
    sleep(0.5)

def boot():
  download_and_install_update_if_available()
  start()
  boot()

