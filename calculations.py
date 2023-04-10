import requests
#import matplotlib.pyplot as plt
import datetime
import json
import time
import schedule

price = [0]*24

def getPrices():
    global price
    f = open("request.json", "r")
    fileDate = f.read(5)
    f.seek(6,0) # Läser filen från efter datumet
    fileContent = f.read()
    f.close()

    price = []

    today = datetime.date.today()

    year = str(today.year)

    date = f'{today.month:02d}-{today.day:02d}'

    region = "SE1"

    if fileDate != date:
        data = requests.get(f'https://www.elprisetjustnu.se/api/v1/prices/{year}/{date}_{region}.json')
        dataJson = data.json()

        f = open("request.json", "w")
        f.write(f'{date}\n') # 6 chars
        f.write(data.text)
        f.close()

    else:
        dataJson = json.loads(fileContent)

    for i in range(24):
        price.append(dataJson[i]["SEK_per_kWh"])

    return price


# 0.15212 kr / kWh

maxWatt = 60
constantPrice = 20

def calculateBrightness() -> float:
    global price
    timeNow = datetime.datetime.now().hour
    currentPrice = price[timeNow]

    # Omskrivning av:
    # kWh-priset * (Watt/1000) * (en månad) = konstantPris
    #                  ^ kWh      ^ 24*30
    watt = 1000 * constantPrice / (currentPrice * 24 * 30)

    watt = min(watt,maxWatt)

    percentage = watt / maxWatt # Det här kommer nog inte funka, räkna ut på nåt annat sätt

    return percentage



def startSchedule():
    getPrices()

    schedule.every(10).seconds.do(getPrices)

    schedule.every(1).seconds.do(calculateBrightness)

    while True:
        schedule.run_pending()
        time.sleep(1)
