from machine import Pin
import time
led1 = Pin (1, Pin.OUT)
led2 = Pin (2, Pin.OUT)
pul1 = Pin (28, Pin.IN)
pul2 = Pin (27, Pin.IN)
while 1:
 if pul1.value() == 1:
  led1.on()
 else:
  led1.off()
  
  if pul2.value() == 1:
   if led2.value() == 1:
    led2.off()
    time.sleep_ms(500)
   if led2.value() == 0:
    led2.on()
    time.sleep_ms(500)