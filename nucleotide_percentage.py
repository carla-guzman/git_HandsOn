#!/usr/bin/env python

# Import required modules
import sys
import re
from argparse import ArgumentParser

# Define command-line arguments
parser = ArgumentParser(
    description="Calculate nucleotide percentages in a DNA or RNA sequence")

parser.add_argument( "-s", "--seq", type=str, required=True, help="Input sequence")

# Display help if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse command-line arguments
args = parser.parse_args()

# Convert sequence to upper-case
seq = args.seq.upper()

# Validate sequence
if not re.search('^[ACGTU]+$', seq):
    print("Invalid sequence")
    sys.exit(1)

# Invalid sequence containing both T and U
if 'T' in seq and 'U' in seq:
    print("Invalid sequence: contains both T and U")
    sys.exit(1)

# Calculate nucleotide percentages
length = len(seq)

print(f"Sequence length: {length}")

for nucleotide in ["A", "C", "G", "T", "U"]:
    count = seq.count(nucleotide)
    percentage = (count / length) * 100
    print(f"{nucleotide}: {percentage:.2f}%")
