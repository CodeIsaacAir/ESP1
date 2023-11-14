import machine
import time

class LED:
    def __init__(self):
        self.led_pins = [27, 26, 25]  
        self.leds = [machine.Pin(pin, machine.Pin.OUT) for pin in self.led_pins]

    def control_led(self,number):
        if number == 10:
            self.leds[0].on()
            self.leds[1].off()
            self.leds[2].off()
        elif number == 30:
            self.leds[0].off()
            self.leds[1].on()
            self.leds[2].off()
        elif number == 50 or number==60 or number==70:
            self.leds[0].off()
            self.leds[1].off()
            self.leds[2].on()
        else:
           
            for led in self.leds:
                led.off()

    def blink_all_leds(self,duration, blink_count):
        for _ in range(blink_count):
            for led in self.leds:
                led.on()
            time.sleep(duration)
            for led in self.leds:
                led.off()
            time.sleep(duration)
