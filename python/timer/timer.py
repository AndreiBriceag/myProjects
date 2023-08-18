from playsound import playsound
import time

# ANSI escape sequences: clear text and update timer on the same line in terminal
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) # wait 1s (if not, alarm sounds asap, overriding the timer time)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # we do // to receive a whole number from the division (no decimals)
        seconds_left = time_left % 60 # we do % to rceive the remainder from the division
        
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}") # :02d format time with 2 digits and padded with 0 in front
    
    playsound("timer/alarm.mp3")

minutes = int(input("How many minutes do you want to set:"))
seconds = int(input("How many seconds do you want to set:"))
time_to_wait = minutes * 60 + seconds # start the alarm with time in seconds
alarm(time_to_wait)