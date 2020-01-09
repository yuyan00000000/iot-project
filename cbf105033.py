import time
from machine import Pin, PWM

sound=PWM(Pin(5))
duration = 4  #聲音長度
def tone(sound,note,duration):
    sound.freq(note)
    sound.duty(1000)
    
def playsound(sound,note):
    j = 0
    d=int(1000/duration)
    p=int(d*0.5)
    tone(sound, note, d)

def ping(trigPin, echoPin):
    trig=Pin(trigPin, Pin.OUT)
    echo=Pin(echoPin, Pin.IN)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count=0
    timeout=False
    start=time.ticks_us()
    while not echo.value(): #wait for HIGH
        time.sleep_us(10)
        count += 1
        if count > 100000: #over 1s timeout
            timeout=True
            break
    if timeout: #timeout return 0
        duration=0
    else: #got HIGH pulse:calculate duration
        count=0
        start=time.ticks_us()
        while echo.value(): #wait for LOW
            time.sleep_us(10)
            count += 1
            if count > 2320: #over 400cm range:quit
                break
        duration=time.ticks_diff(time.ticks_us(), start)
    return duration

while True:
    distance=round(ping(trigPin=13,echoPin=15)/58)
    print('%scm' % distance)
    tmp = 1023 - distance*5
    if tmp<0 :tmp = 	988
    elif 273>tmp and tmp>=0 :tmp = 	880
    elif 523>tmp>=273 :tmp = 784
    elif 623>tmp>=523 :tmp = 698
    elif 723>tmp>=623 :tmp = 659
    elif 823>tmp>=723 :tmp = 587
    elif 923>tmp>=823 :tmp = 523
    else: tmp = 330
    playsound(sound, tmp)
    time.sleep(1)
