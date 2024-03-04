"""
Command line arguments
"""

import sys
import cowsay

if len(sys.argv) < 2:
    print("Too few arguments")

for arg in sys.argv[1:]:
    print(f"Hello, {arg}")

cowsay.cow(f"Hello, {sys.argv[1]}")
