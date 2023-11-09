from fhict_cb_01.custom_telemetrix import CustomTelemetrix
import time, sys, threading
import requests 

# Constants
BUTTON1PIN = 8  
BUTTON2PIN = 9  
REDLEDPIN = 4
GREENLEDPIN = 5
BLUELEDPIN = 6
YELLOWLEDPIN = 7
BUZZER = 3

# Programs
PROGRAMS = [
    [1, 0, 0, 0],  
    [0, 1, 0, 0],  
    [0, 0, 1, 0],  
    [0, 0, 0, 1]  
]

# Timer Durations
TIMER_DURATIONS = [2, 3, 4, 5]

# Variables
current_program = 0
button_last_state = [1, 1]  
timers = [None] * len(PROGRAMS)
e = 0

# Functions
def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_digital_input_pullup(BUTTON1PIN)
    board.set_pin_mode_digital_input_pullup(BUTTON2PIN)
    board.set_pin_mode_digital_output(REDLEDPIN)
    board.set_pin_mode_digital_output(GREENLEDPIN)
    board.set_pin_mode_digital_output(BLUELEDPIN)
    board.set_pin_mode_digital_output(YELLOWLEDPIN)
    board.set_pin_mode_analog_output(BUZZER)
    board.digital_write(YELLOWLEDPIN, 1)
    board.digital_write(BLUELEDPIN, 0)
    board.digital_write(GREENLEDPIN, 0)
    board.digital_write(REDLEDPIN, 0)
def start_timer(duration, program_index):
    def timer_callback():
        led_states = PROGRAMS[program_index]
        board.digital_write(YELLOWLEDPIN, led_states[0])
        board.digital_write(BLUELEDPIN, led_states[1])
        board.digital_write(GREENLEDPIN, led_states[2])
        board.digital_write(REDLEDPIN, led_states[3])

    timers[program_index] = threading.Timer(duration, timer_callback)
    timers[program_index].start()

def loop():
    time.sleep(0.01)
    button1_state = board.digital_read(BUTTON1PIN)
    button2_state = board.digital_read(BUTTON2PIN)

    if button1_state and not button1_state[0] and button1_state != button_last_state[0]:
        global current_program
        current_program = (current_program + 1) % len(PROGRAMS)
        
        led_states = PROGRAMS[current_program]
        board.digital_write(YELLOWLEDPIN, led_states[0])
        board.digital_write(BLUELEDPIN, led_states[1])
        board.digital_write(GREENLEDPIN, led_states[2])
        board.digital_write(REDLEDPIN, led_states[3])

        if timers[current_program] is not None:
            timers[current_program].cancel()

    if button2_state and not button2_state[0] and button2_state != button_last_state[1]:
        start_timer(TIMER_DURATIONS[current_program], current_program)
        
        remaining_time = TIMER_DURATIONS[current_program]
        while remaining_time > 0:
            print(f"Timer for Program {current_program + 1}: {remaining_time} seconds", end="\r")
            time.sleep(1)
            remaining_time -= 1
        else:
            global response
            global e
            print("\nThe pizzas are ready!")
            data = { 'status': "Pizza done" }
            response = requests.post('http://192.168.0.101:5000/status', json = data)
            while e < 3:
                board.analog_write(BUZZER, 10)
                time.sleep(0.25)
                board.analog_write(BUZZER, 0)
                time.sleep(0.25)
                e += 0.5
            e = 0
    button_last_state[0] = button1_state
    button_last_state[1] = button2_state

# Main program
setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:  # Ctrl+C
        print('shutdown')
        board.shutdown()
        sys.exit(0)
