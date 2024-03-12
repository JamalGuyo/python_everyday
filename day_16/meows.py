"""
argparser
"""

import argparse

parser = argparse.ArgumentParser("Meow like a cat")
parser.add_argument("-n", default=1, type=int, help="Number of times to meow")
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
