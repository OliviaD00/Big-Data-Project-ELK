import random, time
from datetime import datetime

types = ["emerg", "error", "notice", "debug"]
probas= [0.05   , 0.1    , 0.7     , 0.15   ]

def generateType():
    val = random.random()
    for type, proba in zip(types, probas):
        if val < proba: return type
        else: val -= proba

    return "error"

while 1:
    type = generateType()
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    msg = "{} [{}]: blabla".format(date,type)
    print(msg)

    time.sleep(0.5)