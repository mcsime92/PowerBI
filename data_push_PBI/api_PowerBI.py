import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

##class for data_generation

items = ['terrible', 'bad', 'OK', 'average', 'decent', 'good', 'great', 'ideal', 'perfect']

# Generates random variables
def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20,200)
    price = random.randint(10, 100)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()
    tolerance = 55
    chosen_word = random.choice(items)
    price_by_speed = price/speed

    return [surr_id, speed, price, price_by_speed, tolerance, date, time, chosen_word]


if __name__ == '__main__':

    REST_API_URL = 'ADD HERE YOUR URL'

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["surr_id", "speed", "price", "price_by_speed", "tolerance", "date", "time", "chosen_word"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        time.sleep(10)
