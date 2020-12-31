import random, time

types = ["emerg", "error", "notice", "debug"]
probas= [0.05   , 0.1    , 0.7     , 0.15   ]

while 1:
    val = random.random()
    for type, proba in zip(types, probas):
        #print("{} vs {} ({})".format(val, proba, type))
        if val < proba:
            print(type)
            break
        else:
            val -= proba
    time.sleep(0.5)