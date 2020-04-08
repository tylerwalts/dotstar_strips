#!/usr/bin/python3
# CircuitPython demo - Dotstar
import time
import adafruit_dotstar
import board
import digitalio
import random

# Define the LED strips
strip_length = 32
num_strips = 8
num_pixels = strip_length * num_strips
pixels = adafruit_dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=0.1, auto_write=False)

# Define the PIR sensor
pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT
person_present = False

# For changing speed & brightness over time
bright_min = 0
bright_max = 0.8
bright_inc = 0.1 # % increment
bright_step = (bright_max - bright_min) * bright_inc
bright_value = bright_min # Start at the dimmest

wait_max = 10
wait_min = 1
wait_inc = 0.1 # % increment
wait_step = (wait_max - wait_min) * wait_inc
wait_value = wait_max # Start at the slowest

idle_count = 0
idle_count_max = 200

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
LIGHTBLUE = (8, 107, 255)
LIGHTBLUE2 = (8, 105, 205)
LIGHTBLUE3 = (11, 9, 210)
LIGHTBLUE4 = (17, 88, 213)
LIGHTBLUE5 = (12, 27, 119)
LIGHTBLUE6 = (16, 37, 114)
LIGHTBLUE7 = (11, 100, 213)
LIGHTBLUE8 = (12, 31, 124)
LIGHTBLUE9 = (17, 70, 111)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MERLOT = (20, 4, 16)

def init():
    check_pir()

def turn_it_up():
    global bright_value
    global bright_step
    global bright_max
    global wait_value
    global wait_step
    global wait_min
    if (bright_value + bright_step <= bright_max):
        bright_value = bright_value + bright_step
        pixels = adafruit_dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=bright_value, auto_write=False)
        print('Brightness is at: ' + str(bright_value))
    else:
        print('Brightness is maxed at: ' + str(bright_value))
    if (wait_value - wait_step >= wait_min):
        wait_value = wait_value - wait_step
        print('Wait value is at: ' + str(wait_value))
    else:
        print('Wait value is at min: ' + str(wait_value))

def turn_it_down():
    global bright_value
    global bright_step
    global bright_min
    global wait_value
    global wait_step
    global wait_max
    if (bright_value - bright_step >= bright_min):
        bright_value = bright_value - bright_step
        pixels = adafruit_dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=bright_value, auto_write=False)
        print('Brightness is at: ' + str(bright_value))
    else:
        print('Brightness is at min: ' + str(bright_value))
    if (wait_value + wait_step <= wait_max):
        wait_value = wait_value + wait_step
        print('Wait value is at: ' + str(wait_value))
    else:
        print('Wait value is at max: ' + str(wait_value))

def check_pir():
    global person_present
    global idle_count
    value = pir.value
    if value:
        if person_present:
            print('Person already detected, still here...')
        else:
            print('*** Detected Person! ***')
            person_present = True
            blink(ORANGE, 0.1, 2)
        turn_it_up()
        idle_count = 0
    else:
        if person_present:
            if idle_count > (idle_count_max / 2):
                print('Idle count is more than half of max: ' + str(idle_count) + 'Lost person - Goodbye!')
                person_present = False
                blink(BLUE, 0.1, 2)
            else:
                print('No motion detected. Idle Count: ' + str(idle_count))
        else:
            print('Nobody here. Idle Count = ' + str(idle_count))
        turn_it_down()
        idle_count = idle_count + 1

def blink(color, wait, times):
    init()
    for i in range(times):
        color_fill(color, wait)
        color_fill(BLACK, wait)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def color_fill(color, wait):
    init()
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)

def slice_xmas(wait):
    init()
    pixels[::2] = [RED] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [GREEN] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)

def slice_alternating(wait):
    init()
    pixels[::2] = [RED] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [ORANGE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [YELLOW] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [GREEN] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [TEAL] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [CYAN] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [BLUE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [PURPLE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [MAGENTA] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [WHITE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)

def slice_rainbow(wait):
    global num_pixels
    init()
    pixels[::6] = [RED] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[1::6] = [ORANGE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[2::6] = [YELLOW] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[3::6] = [GREEN] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[4::6] = [BLUE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[5::6] = [PURPLE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)

def color_cycle_opposite_ends(color):
    init()
    for i in range(strip_length):
        #pixels[i] = color
        for j in range(num_strips):
            pixels[i+(strip_length*j)] = color
        pixels.show()
        time.sleep(0.001 * wait_value)

def color_cycle_bottom_up(color):
    init()
    for i in range(strip_length):
        for j in range(num_strips):
            pixels[(strip_length*j)-i] = color
        pixels.show()
        time.sleep(0.001 * wait_value)

def color_cycle2(color, color2):
    init()
    for i in range(num_pixels):
        pixels[i] = color
        pixels[num_pixels-i] = color2
        pixels.show()
        time.sleep(0.001 * wait_value)

def color_cycle(color):
    init()
    for i in range(num_pixels):
        pixels[i] = color
        pixels.show()
        time.sleep(0.001 * wait_value)

def color_shot(color):
    init()
    for i in range(num_pixels):
        pixels[i] = color
        pixels.show()
        time.sleep(0.001 * wait_value)

def rainbow_cycle(wait):
    init()
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

def single_up(color, wait, strip, solid = False, strip_height = strip_length):
    init()
    global strip_length
    color_fill(BLACK, wait)
    start_index = strip_length * (strip - 1)
    pixels[start_index] = color
    pixels.show()
    time.sleep(wait)
    for i in range(strip_height - 1):
        pixels[start_index + i] = color
        if not solid: pixels[start_index + i - 1] = BLACK
        pixels.show()
        time.sleep(wait)

def single_down(color, wait, strip, solid = False):
    init()
    global strip_length
    color_fill(BLACK, wait)
    start_index = (strip - 1) * strip_length
    pixels[start_index] = color
    pixels.show()
    time.sleep(wait)
    for i in range(strip_length):
        pixels[start_index - i] = color
        if not solid: pixels[start_index - i + 1] = BLACK
        pixels.show()
        time.sleep(wait)

def sparkle_pulse(sparkle_range):
    init()
    for i in range(sparkle_range):
        color = (int(255 * (i/sparkle_range)), int(255 * (i/sparkle_range)), int(255 * (i/sparkle_range)))
        print('color: ' + str(color))
        sparkle(i * 5, color, 0.05 * (sparkle_range - i + 1) )
    sparkle(40, WHITE, 0.04)

def sparkle(num_flashes, color, wait):
    for i in range(num_flashes):
        random_fill(color, 9)
        time.sleep(wait)

def random_fill(color, odds_threshold = 5):
    global num_pixels
    color_fill(BLACK, 0.001)
    for i in range(num_pixels):
        light_odds = random.randint(0,10)
        if (light_odds > odds_threshold):
            pixels[i] = color
    pixels.show()

def fire(flames, wait):
    global strip_length, num_strips
    init()
    for i in range(flames):
        strip = random.randint(1,num_strips)
        color = random.randint(0,2)
        strip_height = random.randint(5, strip_length)
        colors = [RED, ORANGE, YELLOW]
        single_up(colors[color], wait, strip, True, strip_height)

def merlot(wait):
    init()
    for i in range(6):
        strip = random.randint(1,4)
        single_up(MERLOT, wait, strip, True)

def rain(drops):
    global num_strips
    init()
    for i in range(drops):
        strip = random.randint(1,num_strips)
        color = random.randint(0,11)
        wait = random.uniform(0, 0.04)
        colors = [BLUE, WHITE, LIGHTBLUE, LIGHTBLUE, LIGHTBLUE2, LIGHTBLUE3, LIGHTBLUE4, LIGHTBLUE5, LIGHTBLUE6, LIGHTBLUE7, LIGHTBLUE8, LIGHTBLUE9]
        single_down(colors[color], wait, strip, False)

def pulse():
    for i in range(4,25):
        color_fill(((i*10), (i*10), (i*10)), 0.01)

    for i in range(4,25):
        color_fill(((250-(i*10)), (250-(i*10)), (250-(i*10))), 0.01)

def circle(color, wait, times, blackout = True):
    global strip_length
    global num_strips
    init()
    index = 0
    pixels[index] = color
    pixels.show()
    time.sleep(wait)
    for i in range(times):
        for j in range(strip_length - 1):
            last_index = index
            index = index + 1
            pixels[index] = color
            if blackout: pixels[last_index] = BLACK
            pixels.show()
            time.sleep(wait)
        for j in range(num_strips - 1):
            last_index = index
            index = index + 1
            pixels[index] = color
            if blackout: pixels[last_index] = BLACK
            pixels.show()
            time.sleep(wait*2)
        for j in range(strip_length - 1):
            last_index = index
            index = index + 1
            pixels[index] = color
            if blackout: pixels[last_index] = BLACK
            pixels.show()
            time.sleep(wait)
        for j in range(num_strips - 1):
            last_index = index
            index = index - (strip_length * 2) + 1
            pixels[index] = color
            if blackout: pixels[last_index] = BLACK
            pixels.show()
            time.sleep(wait*2)

def xmas_main():
    slice_xmas(0.05)
    color_cycle2(GREEN, RED)
    color_cycle(GREEN)
    color_cycle(RED)
    color_cycle(WHITE)

foo = False

i = 0
while True:
    print('Loop: ' + str(i))
    i=i+1
    check_pir()

    print("idle count= " + str(idle_count) + ", max = " + str(idle_count_max))
    if idle_count < idle_count_max:

        #circle(GREEN, 0.01, 1, False)

        pulse()

        sparkle_pulse(5)

        color_fill(WHITE, 3)

        fire(60, 0)

        pulse()

        rain(15)

        slice_alternating(0.5)

        color_cycle2(BLACK, BLACK)

        color_cycle2(MERLOT, WHITE)

        #TODO: make a color_cycle_from_ends function, first half is cool. skip 2nd.
        #Exa: color_cycle_ends(WHITE, WHITE)
          #color_cycle2(WHITE, WHITE)

        color_cycle_bottom_up(ORANGE)
        color_cycle_bottom_up(BLACK)
        color_cycle_bottom_up(YELLOW)

        #color_cycle_opposite_ends(GREEN)
        pulse()

        #slice_rainbow(0.05)
        rainbow_cycle(0.05)

    else:
        color_fill(BLACK, 1)



