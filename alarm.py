from threading import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from pygame import mixer
import tkinter as tk
from datetime import datetime
from datetime import timedelta
from time import sleep
import time
import math
import multiprocessing
from playsound import playsound
#colors
bg_color = '#ffffff'
co1 = "#566FC6" #blue
co2 = "#000000" #black

#window
window = Tk()
window.title("Alarm Clock")
window.geometry('550x430')
window.configure(bg='#002B5B')

#frame up
frame_line = Frame(window, width=550, height=5, bg='#002B5B')
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=550, height=350, bg='#f6f6f6')
frame_body.grid(row=1, column=0)
frame_body2 = Frame(window, width=550, height=80, bg='#f6f6f6')
frame_body2.grid(row=2, column=0)
def clear_frame():
   for widgets in frame_body2.winfo_children():
      widgets.destroy()
'''#configuring frame body
img = Image.open('logo.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)
'''
WIDTH = 250
HEIGHT = 250
canvas = tk.Canvas(frame_body, width=250, height=250, bg="#f6f6f6" ,borderwidth=0.1)
canvas.place(x=15, y=40)

def update_clock():
    canvas.delete("all")
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec
 
    # Draw clock face
    canvas.create_oval(2, 2, WIDTH, HEIGHT, outline="#002B5B", width=2)
 
    # Draw hour numbers
    for i in range(12):
        angle = i * math.pi/6 - math.pi/2
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y-10, text=str(i+12), font=("Helvetica", 12),fill="#002B5B")
        else:
            canvas.create_text(x, y, text=str(i), font=("Helvetica", 12),fill="#002B5B")
 
    # Draw minute lines
    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
        x2 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="#002B5B", width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="#002B5B", width=1)
 
    # Draw hour hand
    hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
    hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, hour_x, hour_y, fill="#002B5B", width=6)
 
    # Draw minute hand
    minute_angle = (minute + second/60) * math.pi/30 - math.pi/2
    minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
    minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, minute_x, minute_y, fill="#002B5B", width=4)
 
    # Draw second hand
    second_angle = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6 * WIDTH/2 * math.cos(second_angle)
    second_y = HEIGHT/2 + 0.6 * WIDTH/2 * math.sin(second_angle)
    canvas.create_line(WIDTH/2, HEIGHT/2, second_x, second_y, fill="red", width=2)
    canvas.after(1000, update_clock)
update_clock()
#app_image = Label(frame_body, height=100, image=img, bg=bg_color)
#app_image.place(x=10, y=10)

name = Label(frame_body, text = "Alarm Clock", height=1, font=('Ivy 18 bold'), bg='#f6f6f6',fg="#002B5B")
name.place(x=300, y=10)

hour = Label(frame_body, text = "hour", height=1,font=('arial 10 bold'), bg="#f6f6f6", fg="#002B5B")
hour.place(x=300, y=50)
c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23")
c_hour.current(0)
c_hour.place(x=300, y=70)

min = Label(frame_body, text = "min", height=1, font=('arial 10 bold'), bg='#f6f6f6', fg="#002B5B")
min.place(x=350, y=50)
c_min = Combobox(frame_body, width=2, font=('arial, 15'))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=350, y=70)

sec = Label(frame_body, text = "sec", height=1, font=('arial 10 bold'), bg='#f6f6f6', fg="#002B5B")
sec.place(x=400, y=50)
c_sec = Combobox(frame_body, width=2, font=('arial 15'))
c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_sec.current(0)
c_sec.place(x=400, y=70)

'''period = Label(frame_body, text = "period", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
period.place(x= 277, y=40)
c_period = Combobox(frame_body, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=280, y=58)'''
alarmop = IntVar()
#AddAlarmButton
 # Ringtone Label.
 # Ringtones list.
ringtones_list = ['calling', 'wakeup', 'wind-up', 
'twirling_intime', 'morning-joy']

# Ringtones Path.
ringtones_path = {
    'calling': 'Ringtones/calling.mp3',
    'wakeup': 'Ringtones/wakeup.mp3',
    'wind-up': 'Ringtones/wind-up-clock-alarm.mp3',
    'twirling_intime': 'Ringtones/twirling_intime.mp3',
    'morning-joy': 'Ringtones/morning-joy.mp3'
}

ringtone_label = Label(frame_body, text = "Ringtones", height=1, font=('arial 12 bold'), bg='#f6f6f6', fg="#002B5B")
ringtone_label.place(x=300, y=110)

# Ringtone Combobox(Choose the ringtone).
ringtones = StringVar()
ringtones_combobox = ttk.Combobox(frame_body, width=16, height=8, textvariable=ringtones, font=("arial",10),background='white',foreground='black')
ringtones_combobox['values'] = ringtones_list
ringtones_combobox.current(0)
ringtones_combobox.place(x=300,y=140)

# Title or Message Label.
message_label = Label(frame_body, text = "Message", height=1, font=('arial 12 bold'), bg='#f6f6f6', fg="#002B5B")
message_label.place(x=300, y=170)

# Message Entrybox: This Message will show, when
# the alarm will ringing.
message = StringVar()
message_entry = Entry(frame_body, textvariable=message, font=("arial",10), width=30,bg='white',fg='black')
message_entry.insert(0, 'Wake Up')
message_entry.place(x=300, y=200)

#Call Alarm
def activate_alarm():
    t = Thread(target=addAlarm)
    t.start()
B = Button(frame_body, text ="Set Alarm", font=('arial 12 bold'),command = activate_alarm,bg='#159895',fg='white',height=1,width=14)
B.place(x = 320, y=240)

'''def alarm():
    while True:
        control = selected.get()
        print(control)

        alarm_hour=c_hour.get()
        alarm_minute = c_min.get()
        alarm_sec = c_sec.get()
        #alarm_period = c_period.get()
        #alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        #period = now.strftime("%p")

        if control == 1:
            #if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break!")
                            sound_alarm()
        sleep(1)
'''
def addAlarm():
    alarm_hour=c_hour.get()
    alarm_minute = c_min.get()
    alarm_sec = c_sec.get()
    set_alarm_time = f"{alarm_hour}:{alarm_minute}:{alarm_sec}"
    AlarmLabel = Label(frame_body, font=('arial 12'),text=f'Alarm time: {alarm_hour}:{alarm_minute}:{alarm_sec}', bg='#002B5B',fg='#f6f6f6')
    AlarmLabel.place(x=320, y=300)
    # sleep for 1s to update the time every second
    #playsound(ringtones_path[ringtones_combobox.get()])

    while True:
        time.sleep(1)
        now = datetime.now()
        hour = now.strftime("%H")
        #print(hour,alarm_hour)
        #print(hour==alarm_hour)
        minute = now.strftime("%M")
        second = now.strftime("%S")
        if hour == alarm_hour:
            print(hour,alarm_hour)
            if minute == alarm_minute:
                print("Time to take a break!")
                #RemainingLabel = Label(frame_body2, font=('arial 10'), fg='red',bg='#f6f6f6')
                #RemainingLabel.place(x=345, y=1,width=20,height=10)
                playsound(ringtones_path[ringtones_combobox.get()])
                #print(ringtones_path[ringtones_combobox.get()])
                #sound_alarm()
                #process = multiprocessing.Process(target=playsound, args=(ringtones_path[ringtones_combobox.get()],))
                #process.start()
                # Messagebox: This messagebox will show, when the
                # alarm will ringing.
                messagebox.showinfo("Alarm",f"{message_entry.get()}, It's {set_alarm_time}")
                #process.terminate()
                break
        remaining_time(set_alarm_time)
def remaining_time(set_alarm_time):
    clear_frame()
    alarm_hour=c_hour.get()
    alarm_minute = c_min.get()
    alarm_sec='00'
    # Get current time
    time.sleep(1)
    actual_time = datetime.now().strftime("%H:%M:%S")
    FMT = '%H:%M:%S'
    # get time remaining
    #datetime.fromtimestamp()
    print(set_alarm_time)
    print(actual_time)
    time_remaining = datetime.strptime(set_alarm_time, FMT) - datetime.strptime(actual_time, FMT)
    print(time_remaining.days)
    print(remaining_time)
    # displays time remaining
    RemainingLabel = Label(frame_body, font=('arial 11'),text='Remaining time:', fg='red',bg='#f6f6f6')
    RemainingLabel.place(x=320, y=325)
    RemainingLabel = Label(frame_body2, font=('arial 10'),text=f'{time_remaining}', fg='red',bg='#f6f6f6')
    RemainingLabel.place(x=345, y=1)
    # Check whether set alarm is equal to current time
    #R1 = Radiobutton(frame_body, text=alarm_hour+":"+alarm_minute, variable=alarmop, value=1,command=activate_alarm)
    #R1.pack( anchor = W )
 # Ringtone Label.
 # Ringtones list.
window.mainloop()