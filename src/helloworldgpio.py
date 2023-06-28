# External module imports
import RPi.GPIO as GPIO
import time


def main():
    print("Hello LED")

    ledPin = 9

    print("Setting Broadcom Mode")
    # Pin Setup:
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

    GPIO.setup(ledPin, GPIO.OUT) 

    print("Here we go! Press CTRL+C to exit")
    try:
        while True:
            print ("OFF")
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(1.00)
            print ("ON")            
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(1.00) 
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO

if __name__ == '__main__':
    main()