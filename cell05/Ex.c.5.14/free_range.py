#!/usr/bin/env python3
import sys

# Check if the number of arguments is 2
if len(sys.argv) != 3:
    print("none")
else:
    # Get the two numbers from command-line arguments
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    # Create the range and convert it to a list
    result = list(range(start, end + 1))
    
    # Print the result
    print(result)
