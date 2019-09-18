# Edit line 6 to match your chosen GPIO pin
print 'Pi off'
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
GPIO.output(21,GPIO.LOW)
GPIO.cleanup()