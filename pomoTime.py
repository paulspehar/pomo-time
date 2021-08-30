#! /usr/bin/python

# pomoTime.py - Pomodoro timer

import time

#get user input (time) as string and convert to int
# t = int(input("How many seconds do you want to set the time for? "))

# # decrease time by 1 sec until 0 secs
# while t:
#     mins = t // 60 # convert secs to mins floor div //
#     secs = t % 60 # t modulo 60 to handle remainder secs
#     timer = '{:02d}:{:02d}'.format(mins, secs) # 2 width, 0 padding, digit value
#     print(timer, end="\r") # print timer on same line (overwrite previous)
#     time.sleep(1)
#     t -= 1 # sleep for 1 min between loops
# print('Boom!!!')

print("Pomodoro starts now!")
for i in range(4):
    t = 25*60 # 25 mins
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(" " + timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Break Time!!!")
    t = 5*60
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(" " + timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Back to Work!!!")