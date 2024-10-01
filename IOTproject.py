import telegram
import serial
import requests
import cv2
import time
import datetime

cap = cv2.VideoCapture(0)
try:
    arduinodata = serial.Serial('/dev/ttyACM0',9600)
except:
    print("can not find data D")
bot = telegram.Bot(token='6110698173:AAF4lnl-ZcRQ5pKvlzGPIMJoYmxaAmgg0dY')

bot.send_message(chat_id="-1001826468115", text='Hello, World!')



d1={"14957173172": "main","221152145102": "melvin"}
d2=d1.values()

# for i in d2:
#     print(i)
ad=False



while True:
    
    try:
        data1= arduinodata.readline()
    except:
        print("can not read")


    print(data1)
    datad = data1.decode()

    datad = str(datad)
    datad = datad.strip()
    #print(datad)
    #print(type(datad))
    datad = datad.replace(" ","")
    print(datad)

    for i in d1:
        if (i==datad):
            ad=True
            dat=d1[i]
        # else:
        #     ad = False
    _, frame = cap.read()       
        
    if (ad ==True):
        text1 = "welcome " + dat
        bot.send_message(chat_id="-1001826468115", text = text1)
        current_time = datetime.datetime.now().strftime("%d-%m-%Y-----%H-%M-%S")

        dataTele = " person dectected in " + current_time
        cv2.imwrite('/home/nano/iot_pro/iot_img/'+dataTele+".png", frame)
        bot.send_message(chat_id="-1001826468115", text = dataTele)


        #bot.send_photo(chat_id = "-1001826468115" , photo=open('/home/nano/iot_pro/iot_img/'+dataTele+'.png', 'rb'))



        print("Authorised person")
        print("welcome",dat)

        
    elif(ad ==False):
        bot.send_message(chat_id="-1001826468115", text='Unauthorised person')
        print("Unauthorised person")
        #bot.send_message(chat_id="-1001826468115", text='permision required')
        current_time = datetime.datetime.now().strftime("%d-%m-%Y-----%H-%M-%S")
        
        
        time.sleep(0.5)
        dataTele = "dectected in " + current_time
        cv2.imwrite('/home/nano/iot_pro/iot_UN_img/'+dataTele+".png", frame)
        bot.send_message(chat_id="-1001826468115", text = dataTele)

        #bot.send_photo(chat_id = "-1001826468115" , photo=open('/home/nano/iot_pro/iot_UN_img/'+dataTele+'.png', 'rb'))
    
    ad = False
    cv2.imshow("Camera", frame)


    if cv2.waitKey(1) == ord('q'):

        break



cap.release()
cv2.destroyAllWindows()







