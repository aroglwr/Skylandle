import schedule
import time

import urllib.request as rq
import json
import random

def updateAns():
    with open("ans.json", mode="r") as f:
        data = json.load(f)
    with open("skylander.json", mode="r", encoding="utf-8") as t:
        sl = json.load(t)["keys"]
    
    latest = (int(list(data)[-1]) + 1)
    char = sl[str(random.randint(0, len(sl)-1))]

    data[latest] = char

    with open("ans.json", mode="w") as f:
        json.dump(data, f)
    print(f"New answer is {char}")


schedule.every().day.at("23:00:00").do(updateAns)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
