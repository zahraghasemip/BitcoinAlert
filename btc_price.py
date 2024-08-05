import cryptocompare
from time import sleep
from pygame import mixer
import pyttsx3

mixer.init()
engine = pyttsx3.init()

tresh_down = 51000
tresh_up = 51050
treshold = 50

while True:
    btc_price = cryptocompare.get_price('BTC', currency='USD')["BTC"]["USD"]
    if btc_price < tresh_down :
        print("btc went low", btc_price)
        tresh_up -= treshold
        tresh_down -=treshold
        mixer.music.load ( "data/beep.mp3" )
        mixer.music.play()
        engine.say("bitcoin price is ()".format(btc_price))
        engine.runAndWait()
    elif btc_price > tresh_up :
        print("btc went high", btc_price)
        tresh_up += treshold
        tresh_down +=treshold
        mixer.music.load( "data/beep.mp3" )
        mixer.music.play()
        engine.say("bitcoin price is ()".format(btc_price))
        engine.runAndWait()
    else:
        print(tresh_down,"<",btc_price,"<",tresh_up)
    sleep(7)

