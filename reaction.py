from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_buttom = Buttom(15)
left_buttom = Buttom(14)

left_name = input('left player name is ')
right_name = input('right player name is ')

def pressed(button):
    global start_time
    reaction_time = time() - start_time
    if button.pin.number == 14:
        print(f"{left_name} won the game! Reaction time: {reaction_time:.3f} seconds")
    else:
        print(f"{right_name} won the game! Reaction time: {reaction_time:.3f} seconds")
    exit()

led.on()
sleep(uniform(5, 10))
led.off()

start_time = time()
  
right_button.when_pressed = pressed
left_button.when_pressed = pressed

exit()
