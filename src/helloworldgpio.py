import RPi.GPIO as GPIO
import time


def main():
    led_pin = 14

    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setwarnings(False)
    GPIO.setup(led_pin, GPIO.OUT) 

    print("Press CTRL+C to exit")
    try:
        while True:
            print ("Led is ON")            
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(1.00) 
            
            print ("Led is OFF")
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(1.00)
            
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO

if __name__ == '__main__':
    main()