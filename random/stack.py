import time
import sys

text_speed = input("What speed? > ")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        if text_speed == "fast":
            time.sleep(0.075)

        elif text_speed == "slow":
            time.sleep(.275)

        elif text_speed == "normal":
            time.sleep(.175)

delay_print("Delay Print 1 \n")
delay_print("Multiple lines at once test. \n")
delay_print("The big brown fox jumped over the lazy dog. \n")