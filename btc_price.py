import cryptocompare
from time import sleep
while True:
    btc_price = cryptocompare.get_price('BTC', currency='USD')["BTC"]["USD"]
    if btc_price < 60000 :
        print("btc went low", btc_price)
    elif btc_price > 60100 :
        print("btc went high", btc_price)
    else:
        print(btc_price)
    sleep(7)

