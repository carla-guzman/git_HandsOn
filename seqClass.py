#!/usr/bin/env python

# Import required modules
import sys, re
from argparse import ArgumentParser

# Define command-line arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Display help if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse command-line arguments
args = parser.parse_args()

# Convert sequence to upper-case
args.seq = args.seq.upper()

# Classify the sequence
if re.search('^[ACGTU]+$', args.seq):

    # DNA contains T but not U
    if 'T' in args.seq and 'U' not in args.seq:
        print('The sequence is DNA')

    # RNA contains U but not T
    elif 'U' in args.seq and 'T' not in args.seq:
        print('The sequence is RNA')

    # Only A,C,G
    elif 'T' not in args.seq and 'U' not in args.seq:
        print('The sequence can be DNA or RNA')

    # Invalid sequence containing both T and U
    else:
        print('The sequence is not DNA nor RNA')

else:
    print('The sequence is not DNA nor RNA')

# Search for a motif if provided
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND FROM MOTIF")
    else:
        print("MOTIF NOT FOUND")

