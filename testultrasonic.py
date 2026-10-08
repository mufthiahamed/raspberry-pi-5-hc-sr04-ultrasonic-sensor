import lgpio
import time

TRIG = 16
ECHO = 21

h = lgpio.gpiochip_open(0)

lgpio.gpio_claim_output(h, TRIG)
lgpio.gpio_claim_input(h, ECHO)

try:
    while True:
        # Make sure trigger starts LOW
        lgpio.gpio_write(h, TRIG, 0)
        time.sleep(0.05)

        # Send 10 microsecond trigger pulse
        lgpio.gpio_write(h, TRIG, 1)
        time.sleep(0.00001)
        lgpio.gpio_write(h, TRIG, 0)

        timeout = time.time() + 0.05

        # Wait for ECHO to go HIGH
        while lgpio.gpio_read(h, ECHO) == 0:
            if time.time() > timeout:
                print("No echo received")
                break
        else:
            pulse_start = time.time()

            timeout = time.time() + 0.05

            # Wait for ECHO to go LOW
            while lgpio.gpio_read(h, ECHO) == 1:
                if time.time() > timeout:
                    print("Echo timeout")
                    break
            else:
                pulse_end = time.time()

                duration = pulse_end - pulse_start
                distance = duration * 17150

                print(f"Distance: {distance:.2f} cm")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped")

finally:
    lgpio.gpiochip_close(h)
