from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_buttom = Buttom(15)
left_buttom = Buttom(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

led.on()
sleep(uniform(5, 10))
led.off()

if button.pin.number == 14:
 print(left_name + ' won the game')
else:
 print(right_name + ' won the game')
  
right_button.when_pressed = pressed
left_button.when_pressed = pressed

exit()
