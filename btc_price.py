import cryptocompare
from time import sleep
from pygame import mixer
mixer.init()


while True:
    btc_price = cryptocompare.get_price('BTC', currency='USD')["BTC"]["USD"]
    if btc_price < 60000 :
        print("btc went low", btc_price)
        mixer.music.load ( "data/beep.mp3" )
        mixer.music.play()
    elif btc_price > 60100 :
        print("btc went high", btc_price)
        mixer.music.load( "data/beep.mp3" )
        mixer.music.play()
    else:
        print(btc_price)
    sleep(7)

