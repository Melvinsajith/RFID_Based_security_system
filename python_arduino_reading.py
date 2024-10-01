import serial
import requests

arduinodata = serial.Serial('/dev/ttyACM0',9600)

import telegram

bot = telegram.Bot(token='6110698173:AAF4lnl-ZcRQ5pKvlzGPIMJoYmxaAmgg0dY')

bot.send_message(chat_id="-1001826468115", text='Hello, World!')

def send_to_telegram(message):

    apiToken = '5994607400:AAEs-UigVBbf1DVR_YCTG4I5kWQDNQPg9eE'
    chatID = '-1001826468115'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

       
while True:
    data1= arduinodata.readline()

    print(data1)
    datad = data1.decode()

    datad = str(datad)
    datad = datad.strip()
    #print(datad)
    #print(type(datad))
    datad = datad.replace(" ","")
    print(datad)


    if ("221152145102" == datad ):

        print("working and open")
        bot.send_message(chat_id="-1001826468115", text='Melvin door opened')

        #send_to_telegram("Melvin door opened ")


