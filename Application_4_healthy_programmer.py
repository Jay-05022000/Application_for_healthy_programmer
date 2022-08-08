#App for healthy programmer

''' programmer will start this application when he/she starts working as a programmer.
This application will remind programmer about certain healty things.such as drinking water,eye exercise and physical exercise.
This application will use music to give acknowledgement about activities.It will also keep tracking of programmer activites.

This application will remind programmer about following things:
1) Drinking water - After every 23 mins from start of application
2) Eye excercise- after every 30 mins from start of application
3) Physical Exercise - After every 41 mins from start of applicationhave to tell user following things:'''


water_count=0
eye_count=0
physical_count=0

import pygame as pg
import time
# function definitions
def water():
    print("hey its water time: ",time.ctime(time.time()))
    global water_count
    water_count+=1
    logfile=open('user_data.txt','a')
    Sw=time.ctime(time.time())
    logfile.write(f'water start time: {Sw} \n')
    pg.mixer.init()  # mixer initialization
    pg.mixer.music.load('water.mp3')  # load music file
    pg.mixer.music.play(-1)

    while (True):
        cmd=input('enter: ')
        if (cmd=='stop'):
            pg.mixer.music.stop()
            # with open('user_data.txt', 'a') as logfile:
            Ew=time.ctime(time.time())
            logfile.write(f'water finished time:{Ew}\n\n')
            logfile.close()
            break
        elif (cmd=='activity'):
            activity()
            continue
        else:
            continue

def physical():
    print("hey its physical exercise time: ", time.ctime(time.time()))
    global physical_count
    physical_count += 1
    logfile = open('user_data.txt', 'a')
    S_ex = time.ctime(time.time())
    logfile.write(f'physical exercise start time: {S_ex} \n')
    pg.mixer.init()  # mixer initialization
    pg.mixer.music.load('physical.mp3')  # load music file
    pg.mixer.music.play(-1)

    while (True):
        cmd = input('enter: ')
        if (cmd == 'stop'):
            pg.mixer.music.stop()
            # with open('user_data.txt', 'a') as logfile:
            E_ex = time.ctime(time.time())
            logfile.write(f'physical exercise finished time:{E_ex}\n\n')
            logfile.close()
            break
        elif (cmd=='activity'):
            activity()
            continue
        else:
            continue
def eye():
    print("hey its eye exercise time: ", time.ctime(time.time()))
    global eye_count
    eye_count += 1
    logfile = open('user_data.txt', 'a')
    S_eye = time.ctime(time.time())
    logfile.write(f'eye exercise start time: {S_eye} \n')
    pg.mixer.init()  # mixer initialization
    pg.mixer.music.load('eye.mp3')  # load music file
    pg.mixer.music.play(-1)

    while (True):
        cmd = input('enter: ')
        if (cmd == 'stop'):
            pg.mixer.music.stop()
            # with open('user_data.txt', 'a') as logfile:
            E_eye = time.ctime(time.time())
            logfile.write(f'eye exercise finished time:{E_eye}\n\n')
            logfile.close()
            break
        elif (cmd=='activity'):
            activity()
            continue
        else:
            continue

def activity():
    print(f'You have done following activities till now:\ndrank water {water_count} times\nDone eye exercise {eye_count} times\nDone physical exercise {physical_count} times')

# Main
print("Hey programmer,Good morning")
start=time.time()     #day starts
print(time.ctime(start))

while(True):
    time_diff=time.time()-start

    if int(time_diff==0) or (int(time_diff)%1380==0):
        water()
    elif (int(time_diff)% 2460==0):
        physical()
    elif (int(time_diff)% 1800==0):
        eye()
    else:
        continue


    

