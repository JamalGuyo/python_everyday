"""
Unpacking
"""


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
coinsDict = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coinsDict), "knuts")


def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(100, 100)
f(galleons=100, sickles=50)
