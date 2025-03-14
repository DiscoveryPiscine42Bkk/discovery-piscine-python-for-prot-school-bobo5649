#!/usr/bin/env python3
import sys

# Check if arguments are passed
if len(sys.argv) == 1:
    print("none")
else:
    # Iterate through all arguments passed
    for arg in sys.argv[1:]:
        if not arg.endswith("ism"):
            print(arg + "ism")
