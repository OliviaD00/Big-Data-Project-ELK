from datetime import datetime
from time import sleep
from json import dumps
from kafka import KafkaProducer
import random

#Kafka
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

#Logs
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

    producer.send('logtest', value=msg)
    print(msg)

    sleep(1)