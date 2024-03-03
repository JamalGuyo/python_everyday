"""
libraries in python
"""

import random

coin = random.choice(["head", "tail"])
number = random.randint(1, 10)

cards = ["King", "Queen", "Jack"]
random.shuffle(cards)
for card in cards:
    print(card)
