# Edit line 6 to match your chosen GPIO pin
print 'pyton off ran'
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.cleanup()