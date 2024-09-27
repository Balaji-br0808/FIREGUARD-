import time
import random  # For simulating smoke detection

# Mock GPIO class to simulate RPi.GPIO functionality
class MockGPIO:
    BCM = None
    OUT = 1
    IN = 0

    def setmode(self, mode):
        print(f"GPIO mode set to {mode}")

    def setup(self, pin, mode):
        print(f"Setup pin {pin} as {'OUTPUT' if mode == self.OUT else 'INPUT'}")

    def input(self, pin):
        # Simulate smoke detection: 1 for smoke detected, 0 for no smoke
        return random.choice([0, 1])  # Randomly return 0 or 1

    def output(self, pin, state):
        if state:
            print(f"Buzzer on pin {pin} activated.")
        else:
            print(f"Buzzer on pin {pin} deactivated.")

    def cleanup(self):
        print("GPIO cleanup done.")

# Mock function to simulate sending a message to the nearest fire station
def send_alert_to_fire_station():
    print("Alert sent to the nearest fire station: Fire detected!")

# Use the mock GPIO class in your project
GPIO = MockGPIO()

# Pin assignments
SENSOR_PIN = 17  # Pin for smoke sensor
BUZZER_PIN = 18   # Pin for buzzer

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set sensor pin as input
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set buzzer pin as output

def main():
    print("Fire Detection System is running...")
    try:
        while True:
            # Read sensor value
            if GPIO.input(SENSOR_PIN):  # Assuming HIGH means smoke detected
                print("Smoke detected! Activating alarm...")
                GPIO.output(BUZZER_PIN, True)  # Turn on buzzer
                send_alert_to_fire_station()  # Send alert to fire station
                time.sleep(5)  # Alarm sound for 5 seconds
                GPIO.output(BUZZER_PIN, False)  # Turn off buzzer
            else:
                print("No smoke detected.")
    
            time.sleep(1)  # Delay before the next reading

    except KeyboardInterrupt:
        print("Program terminated.")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings
        if __name__=="__main__":
            main()
if __name__ == "__main__":
    main()
